from flask import render_template, request, jsonify
from main import app
from flask_login import login_required

@app.route("/table")
@login_required
def table():
    return render_template("table.html")

@app.route("/get_table", methods=["POST"])
def get_table():
    data = request.get_json()

    print(data)
    answer = {
        "status": 200,
        "data": 123
    }

    return jsonify(answer)