from flask import Flask, render_template
from  requests import request

app = Flask(__name__)


@app.route("/<title>")
def index(title):
    return render_template("index.html", title=title)


@app.route("/index")
def index2():
    user = "Ученик"
    return render_template("index2.html", title="Дом", username=user)
 


@app.route('/list_prof/<h>')
def profs(h):
    p = ['Врач', "Строитель", "Инженер", "Летчик", "Космонавт", "Испытатель", "Пилот", "Повар", "Механик"]
    return render_template("list_prof.html", h=h, p=p)

@app.route('/training/<prof>')
def training(prof):
    header = "Инженерные тренажеры" if ("инженер" in prof or "строитель" in prof) else "Научные симуляторы"
    return render_template("training.html", header=header, prof=prof)
 

@app.route('/distribution')
def distribution():
    s = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венкатта Капур",
        "Тедди Сандерс",
        "Шон Бин",
    ]
    return render_template("distribution.html", s=s)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    images = ["https://avatars.mds.yandex.net/i?id=517ce08fcd60ea68f138e17ce2b9635ef6cf21cf-9067430-images-thumbs&n=13",
              "https://raskraska.ot7.ru/img/8/7/3/детские-раскраски-раскраска-инопланетяне-Бесплатно-найти-раскраску-167597.jpg",
              "https://avatars.mds.yandex.net/i?id=fb31c5927e4ff9f2ea5377e837f91477bac1d46c-4834298-images-thumbs&n=13",
              "https://gas-kvas.com/uploads/posts/2023-02/1676708775_gas-kvas-com-p-detskii-risunok-krakozyabra-22.jpg"]
    colors = ["red", "orange", "blue", "green"]
    i = [2, 3]
    if int(age) > 21:
        i = [0, 1]
    c = i[1]
    if sex == "female":
        c = i[0]
    return render_template("table.html", c=colors[c], i=images[c])










