from flask import Blueprint, request, jsonify

from app.database import db
from app.models.student_model import Student

student_bp = Blueprint("student_bp", __name__)

# CREATE STUDENT API
@student_bp.route("/students", methods=["POST"])
def add_student():

    try:

        data = request.get_json()

        # VALIDATIONS

        if not data.get("city_name"):
            return jsonify({
                "error": "City Name is required"
            }), 400

        if not data.get("student_name"):
            return jsonify({
                "error": "Student Name is required"
            }), 400

        if not data.get("dob"):
            return jsonify({
                "error": "DOB is required"
            }), 400

        if not data.get("age"):
            return jsonify({
                "error": "Age is required"
            }), 400

        if not data.get("gmail"):
            return jsonify({
                "error": "Gmail is required"
            }), 400

        if not data.get("branch"):
            return jsonify({
                "error": "Branch is required"
            }), 400

        # CREATE STUDENT OBJECT

        student = Student(

            city_name=data["city_name"],
            student_name=data["student_name"],
            dob=data["dob"],
            age=data["age"],
            gmail=data["gmail"],
            branch=data["branch"]
        )

        # SAVE TO DATABASE

        db.session.add(student)

        db.session.commit()

        return jsonify({
            "message": "Student created successfully"
        }), 201

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
        
# GET ALL STUDENTS API
@student_bp.route("/students", methods=["GET"])
def get_students():

    try:

        students = Student.query.all()

        student_list = []

        for student in students:

            student_data = {

                "id": student.id,
                "city_name": student.city_name,
                "student_name": student.student_name,
                "dob": str(student.dob),
                "age": student.age,
                "gmail": student.gmail,
                "branch": student.branch,
                "created_at": student.created_at
            }

            student_list.append(student_data)

        return jsonify(student_list), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
        
# GET SINGLE STUDENT API
@student_bp.route("/students/<int:id>", methods=["GET"])
def get_single_student(id):

    try:

        student = Student.query.get(id)

        # CHECK STUDENT EXISTS

        if not student:

            return jsonify({
                "error": "Student not found"
            }), 404

        student_data = {

            "id": student.id,
            "city_name": student.city_name,
            "student_name": student.student_name,
            "dob": str(student.dob),
            "age": student.age,
            "gmail": student.gmail,
            "branch": student.branch,
            "created_at": student.created_at
        }

        return jsonify(student_data), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
        
# UPDATE STUDENT API
@student_bp.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    try:

        # FIND STUDENT

        student = Student.query.get(id)

        # CHECK EXISTS

        if not student:

            return jsonify({
                "error": "Student not found"
            }), 404

        # GET REQUEST DATA

        data = request.get_json()

        # UPDATE VALUES

        student.city_name = data.get(
            "city_name",
            student.city_name
        )

        student.student_name = data.get(
            "student_name",
            student.student_name
        )

        student.dob = data.get(
            "dob",
            student.dob
        )

        student.age = data.get(
            "age",
            student.age
        )

        student.gmail = data.get(
            "gmail",
            student.gmail
        )

        student.branch = data.get(
            "branch",
            student.branch
        )

        # SAVE CHANGES

        db.session.commit()

        return jsonify({
            "message": "Student updated successfully"
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
        
# DELETE STUDENT API
@student_bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    try:

        # FIND STUDENT

        student = Student.query.get(id)

        # CHECK EXISTS

        if not student:

            return jsonify({
                "error": "Student not found"
            }), 404

        # DELETE STUDENT

        db.session.delete(student)

        # SAVE CHANGES

        db.session.commit()

        return jsonify({
            "message": "Student deleted successfully"
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500