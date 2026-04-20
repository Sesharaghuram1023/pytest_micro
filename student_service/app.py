from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
students_db = {}


# Home route
@app.route("/")
def home():
    return "Student Service Running 🚀"


# Add student
@app.route("/students", methods=["POST"])
def create_student():
    data = request.json

    student_id = data.get("id")
    name = data.get("name")

    if not student_id or not name:
        return jsonify({"error": "Missing fields"}), 400

    if student_id in students_db:
        return jsonify({"error": "Student already exists"}), 400

    students_db[student_id] = {
        "id": student_id,
        "name": name
    }

    return jsonify(students_db[student_id])


# Get all students
@app.route("/students", methods=["GET"])
def get_all_students():
    return jsonify(list(students_db.values()))


# Get single student
@app.route("/students/<int:student_id>", methods=["GET"])
def get_single_student(student_id):

    if student_id not in students_db:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(students_db[student_id])


# Run app
if __name__ == "__main__":
    app.run(port=5000, debug=True)