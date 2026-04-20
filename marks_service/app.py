from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory storage
marks_db = {}


# Home route
@app.route("/")
def home():
    return "Marks Service Running 🚀"


# Add marks
@app.route("/marks", methods=["POST"])
def add_marks():
    data = request.json

    student_id = data.get("student_id")
    subject = data.get("subject")
    marks = data.get("marks")

    if not student_id or not subject or marks is None:
        return jsonify({"error": "Missing fields"}), 400

    if student_id not in marks_db:
        marks_db[student_id] = []

    marks_db[student_id].append({
        "subject": subject,
        "marks": marks
    })

    return jsonify({
        "message": "Marks added successfully",
        "data": marks_db[student_id]
    })


# Get marks
@app.route("/marks/<int:student_id>", methods=["GET"])
def get_marks(student_id):

    if student_id not in marks_db:
        return jsonify({"error": "Marks not found"}), 404

    return jsonify({
        "student_id": student_id,
        "marks": marks_db[student_id]
    })


# Run app
if __name__ == "__main__":
    app.run(port=5001, debug=True)