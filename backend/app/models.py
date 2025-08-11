from .extensions import db
from datetime import datetime

class Quiz(db.Model):
    __tablename__ = "quizzes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    questions = db.relationship("Question", backref="quiz", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}

class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"), nullable=False)
    text = db.Column(db.Text, nullable=False)
    # optional: points = db.Column(db.Integer, default=1)

    choices = db.relationship("Choice", backref="question", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "quiz_id": self.quiz_id, "text": self.text,
                "choices": [c.to_dict() for c in self.choices]}

class Choice(db.Model):
    __tablename__ = "choices"
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {"id": self.id, "question_id": self.question_id, "text": self.text}
    # NOTE: don't return is_correct in API for frontend when presenting questions

# OPTIONAL: store attempts (if you want)
class Attempt(db.Model):
    __tablename__ = "attempts"
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"), nullable=False)
    score = db.Column(db.Integer)
    total = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
