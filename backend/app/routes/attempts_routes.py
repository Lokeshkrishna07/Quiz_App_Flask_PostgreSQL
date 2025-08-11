from flask import Blueprint, request, jsonify
from .. import db
from ..models import Quiz, Question, Choice, Attempt

attempts_bp = Blueprint("attempts", __name__)

@attempts_bp.route("/submit/<int:quiz_id>", methods=["POST"])
def submit_quiz(quiz_id):
    payload = request.json or {}
    answers = payload.get("answers", {})  # {question_id: choice_id}
    total = 0
    score = 0
    for q in Quiz.query.get_or_404(quiz_id).questions:
        total += 1
        chosen_id = answers.get(str(q.id)) or answers.get(q.id)
        if chosen_id:
            cho = Choice.query.get(chosen_id)
            if cho and cho.is_correct:
                score += 1
    # optional: save attempt
    attempt = Attempt(quiz_id=quiz_id, score=score, total=total)
    db.session.add(attempt)
    db.session.commit()
    return jsonify({"score": score, "total": total})
