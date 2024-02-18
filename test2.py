from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<title>")
def index(title):
    return render_template("index.html", title=title)


@app.route("/index")
def index2():
    user = "Ученик"
    return render_template("index2.html", title="Дом", username=user)
 

@app.route('/training/<prof>')
def training(prof):
    header = "Инженерные тренажеры" if ("инженер" in prof or "строитель" in prof) else "Научные симуляторы"
    return render_template("training.html", header=header, prof=prof)
