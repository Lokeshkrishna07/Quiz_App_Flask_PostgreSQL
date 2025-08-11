from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Quiz, Question, Choice
from .. import db
from datetime import datetime

html_bp = Blueprint("html_bp", __name__)

@html_bp.app_template_global()
def now():
    return datetime.now()

@html_bp.route("/")
def home():
    quizzes = Quiz.query.all()
    return render_template("index.html", quizzes=quizzes, title="Home")

@html_bp.route("/quiz/<int:quiz_id>")
def quiz_detail(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template("quiz_detail.html", quiz=quiz, title=quiz.title)

@html_bp.route("/quiz/<int:quiz_id>/submit", methods=["POST"])
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    total = len(quiz.questions)
    score = 0
    for q in quiz.questions:
        selected_choice_id = request.form.get(f"question_{q.id}")
        if selected_choice_id:
            choice = Choice.query.get(int(selected_choice_id))
            if choice and choice.is_correct:
                score += 1
    return render_template("result.html", score=score, total=total, title="Result")
