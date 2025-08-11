from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Quiz, Question

quizzes_bp = Blueprint("quizzes", __name__)

@quizzes_bp.route("", methods=["GET"])
def list_quizzes():
    quizzes = Quiz.query.all()
    return jsonify([q.to_dict() for q in quizzes])

@quizzes_bp.route("", methods=["POST"])
def create_quiz():
    data = request.json or {}
    q = Quiz(title=data.get("title"), description=data.get("description"))
    db.session.add(q)
    db.session.commit()
    return jsonify(q.to_dict()), 201

@quizzes_bp.route("/<int:quiz_id>", methods=["GET"])
def get_quiz(quiz_id):
    q = Quiz.query.get_or_404(quiz_id)
    # include questions & choices when returning full quiz
    return jsonify({**q.to_dict(), "questions":[ques.to_dict() for ques in q.questions]})
