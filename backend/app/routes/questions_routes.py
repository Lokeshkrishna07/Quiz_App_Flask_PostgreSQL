from flask import Blueprint, request, jsonify
from .. import db
from ..models import Quiz, Question, Choice

questions_bp = Blueprint("questions", __name__)

@questions_bp.route("/<int:question_id>", methods=["GET"])
def get_question(question_id):
    q = Question.query.get_or_404(question_id)
    return jsonify(q.to_dict())

@questions_bp.route("", methods=["POST"])
def create_question():
    data = request.json or {}
    question = Question(quiz_id=data["quiz_id"], text=data["text"])
    db.session.add(question)
    db.session.flush()  # to get question.id
    for c in data.get("choices", []):
        choice = Choice(question_id=question.id, text=c["text"], is_correct=c.get("is_correct", False))
        db.session.add(choice)
    db.session.commit()
    return jsonify(question.to_dict()), 201
