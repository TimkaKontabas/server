from flask import render_template
from main import app


@app.route("/partners")
def partners():
    return render_template("partners.html")