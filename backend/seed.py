from app import create_app, db
from app.models import Quiz, Question, Choice

app = create_app()
with app.app_context():
    python_quiz = Quiz(title="Python Basics Quiz", description="Test your Python knowledge.")
    db.session.add(python_quiz)
    db.session.flush()

    # Question 1
    q1 = Question(quiz_id=python_quiz.id, text="What is the output of print(2 ** 3)?")
    db.session.add(q1)
    db.session.flush()
    db.session.add_all([
        Choice(question_id=q1.id, text="6", is_correct=False),
        Choice(question_id=q1.id, text="8", is_correct=True),
        Choice(question_id=q1.id, text="9", is_correct=False),
        Choice(question_id=q1.id, text="None of the above", is_correct=False),
    ])

    # Question 2
    q2 = Question(quiz_id=python_quiz.id, text="Which of the following is a mutable data type?")
    db.session.add(q2)
    db.session.flush()
    db.session.add_all([
        Choice(question_id=q2.id, text="tuple", is_correct=False),
        Choice(question_id=q2.id, text="list", is_correct=True),
        Choice(question_id=q2.id, text="string", is_correct=False),
        Choice(question_id=q2.id, text="int", is_correct=False),
    ])

    # Question 3
    q3 = Question(quiz_id=python_quiz.id, text="How do you create a function in Python?")
    db.session.add(q3)
    db.session.flush()
    db.session.add_all([
        Choice(question_id=q3.id, text="function myFunc():", is_correct=False),
        Choice(question_id=q3.id, text="def myFunc():", is_correct=True),
        Choice(question_id=q3.id, text="create myFunc():", is_correct=False),
        Choice(question_id=q3.id, text="func myFunc():", is_correct=False),
    ])

    # Question 4
    q4 = Question(quiz_id=python_quiz.id, text="What is the keyword to handle exceptions in Python?")
    db.session.add(q4)
    db.session.flush()
    db.session.add_all([
        Choice(question_id=q4.id, text="try/except", is_correct=True),
        Choice(question_id=q4.id, text="catch/throw", is_correct=False),
        Choice(question_id=q4.id, text="error/handle", is_correct=False),
        Choice(question_id=q4.id, text="handle/except", is_correct=False),
    ])

    # Question 5
    q5 = Question(quiz_id=python_quiz.id, text="Which of these is used to create a comment in Python?")
    db.session.add(q5)
    db.session.flush()
    db.session.add_all([
        Choice(question_id=q5.id, text="//", is_correct=False),
        Choice(question_id=q5.id, text="<!-- -->", is_correct=False),
        Choice(question_id=q5.id, text="#", is_correct=True),
        Choice(question_id=q5.id, text="/* */", is_correct=False),
    ])

    db.session.commit()
    print("Seeded Python Basics Quiz with questions.")
