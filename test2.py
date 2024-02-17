from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<title>")
def index(title):
    return render_template("index.html", title=title)


@app.route("/index")
def index2():
    user = "Ученик"
    return render_template("index2.html", title="Дом", username=user)
