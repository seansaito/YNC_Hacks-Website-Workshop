from flask import render_template, request
from app import app

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    name = ""
    if request.method == "POST":
        name = request.form["name"]
    return render_template("index.html", name=name)
