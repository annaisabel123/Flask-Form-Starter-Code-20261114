from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def result():
    name = request.form.get("name")
    email = request.form.get("email")
    pet = request.form.get("pets")
    music = request.form.getlist("music")
    for key in request.form:
        if not request.form.get(key):
            return render_template("failure.html")
    return render_template("success.html", name = name, email = email, pet = pet, music = music)
