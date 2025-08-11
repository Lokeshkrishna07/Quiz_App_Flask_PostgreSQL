from flask import Flask
from .extensions import db, migrate
from .routes.html_routes import html_bp
from .routes.quizzes_routes import quizzes_bp
from .routes.questions_routes import questions_bp
from .routes.attempts_routes import attempts_bp
from .models import Quiz, Question, Choice  # Import your models so migrations detect them
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(html_bp)
    app.register_blueprint(quizzes_bp, url_prefix="/api/quizzes")
    app.register_blueprint(questions_bp, url_prefix="/api/questions")
    app.register_blueprint(attempts_bp, url_prefix="/api/attempts")

    return app






# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS



# from .routes.html_routes import html_bp

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app(config_class="config.Config"):
#     app = Flask(__name__, instance_relative_config=False)
#     app.config.from_object(config_class)
#     app.register_blueprint(html_bp)


#     CORS(app)  # allow frontend dev to call backend

#     db.init_app(app)
#     migrate.init_app(app, db)

#     # Register blueprints (routes)
#     from .routes import quizzes_bp, questions_bp, attempts_bp
#     app.register_blueprint(quizzes_bp, url_prefix="/api/quizzes")
#     app.register_blueprint(questions_bp, url_prefix="/api/questions")
#     app.register_blueprint(attempts_bp, url_prefix="/api/attempts")

#     @app.route("/health")
#     def health():
#         return {"status": "ok"}

#     return app
