from flask import Flask

from flask_cors import CORS

from app.config import Config
from app.database import db

from app.models.student_model import Student

# IMPORT ROUTES
from app.routes.student_routes import student_bp

def create_app():

    app = Flask(__name__)
    
    CORS(app)

    app.config.from_object(Config)

    db.init_app(app)

    # REGISTER ROUTES
    app.register_blueprint(student_bp)

    with app.app_context():

        db.create_all()

    return app