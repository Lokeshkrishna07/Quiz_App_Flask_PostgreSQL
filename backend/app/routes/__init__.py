from flask import Blueprint

from .quizzes_routes import quizzes_bp
from .questions_routes import questions_bp
from .attempts_routes import attempts_bp

__all__ = ["quizzes_bp", "questions_bp", "attempts_bp"]
