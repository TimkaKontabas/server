from flask import render_template
from main import app
from news_parser import get_news


@app.route("/news")
def news():
    return render_template(
        "news.html", 
        NEWS=get_news())