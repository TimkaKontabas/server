from flask import render_template
from main import app


@app.route("/authors")
def authors():
    return render_template("authors.html")