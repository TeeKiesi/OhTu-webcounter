from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    "a"
    cnt.increase()
    return redirect("/")

@app.route("/set_value", methods=["POST"])
def set_value():
    "a"
    cnt.value = int(request.form["number"])
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset():
    "ada"
    cnt.reset()
    return redirect("/")
