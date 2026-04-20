from flask import Flask, jsonify

app = Flask(__name__)

# dummy marks data (simulate marks_service)
marks_db = {
    1: [
        {"subject": "Math", "marks": 90},
        {"subject": "Science", "marks": 80}
    ]
}


@app.route("/")
def home():
    return "Result Service Running 🚀"


@app.route("/result/<int:student_id>", methods=["GET"])
def get_result(student_id):

    if student_id not in marks_db:
        return jsonify({"error": "No marks found"}), 404

    marks_list = marks_db[student_id]

    total = sum(item["marks"] for item in marks_list)
    count = len(marks_list)
    average = total / count

    result = {
        "student_id": student_id,
        "total": total,
        "average": average,
        "result": "Pass" if average >= 40 else "Fail"
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5002, debug=True)