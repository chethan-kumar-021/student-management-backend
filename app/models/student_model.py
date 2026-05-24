from app.database import db
from datetime import datetime

class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    city_name = db.Column(
        db.String(100),
        nullable=False
    )

    student_name = db.Column(
        db.String(100),
        nullable=False
    )

    dob = db.Column(
        db.Date,
        nullable=False
    )

    age = db.Column(
        db.Integer,
        nullable=False
    )

    gmail = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    branch = db.Column(
        db.String(20),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )