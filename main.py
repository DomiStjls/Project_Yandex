from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

photos = ['mars1.jpg', 'mars2.jpg', 'mars3.jpg', 'mars4.jpg']

@app.route("/results/<nickname>/<int:level>/<float:rating>")
def base(nickname, level, rating):
    return f"""
    <!doctype html>

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Результаты отбора</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

  </head>
    <html lang="en">
  <body>
  <link rel="stylesheet" href="./../../../static/css/style.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <h1>Результаты отбора</h1>
    <h2>Претендент на участие в миссии {nickname}:</h2>
    <p class='s1'>Поздравляем! Ваш рейтинг после {level} отбора</p>
    <p class='s2'>составляет {rating}</p>
    <p class='s3'>Желаем удачи!</p>
  </body>
</html>"""


@app.route("/carousel")
def carousel():
    return """
    <!doctype html>

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Carousel</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

  </head>
    <html lang="en">
  <body>
  <link rel="stylesheet" href="./../../../static/css/style.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <h1 style="color: darkred;">Пейзажи Марса</h1>
    <div id="carouselExampleIndicators" class="carousel slide">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="./../../../static/img/mars1.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="./../../../static/img/mars2.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="./../../../static/img/mars3.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="./../../../static/img/mars4.jpg" class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
  </body>
</html>"""


@app.route("/choice/<planet_name>")
def index0(planet_name):
    return f"""
    <!doctype html>

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Варианты выбора</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

  </head>
    <html lang="en">
  <body>
  <link rel="stylesheet" href="../static/css/style.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <h1>Мое предложение: {planet_name}</h1>
    <h2>Эта планета близка к Земле</h2>
    <p class='p1'>На ней много необходимых ресурсов.</p>
    <p class='p2'>Есть вода и атмосфера.</p>
    <p class='p3'>Она красива.</p>
    <p class='p4'>На ней есть магнитное поле.</p>
  </body>
</html>"""


@app.route("/load_photo", methods=["POST", "GET"])
def load_photo():
    if request.method == "GET":
        return """
        <!doctype html>

    <head>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Варианты выбора</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

    </head>
        <html lang="en">
    <body>
    <link rel="stylesheet" href="../static/css/style.css">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
        
        <h2>Загрузка фотографии для участия в миссии.</h2>
        <form class="photo" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="photo">Выберите файл</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
            </body>
        </html>
        """

    elif request.method == "POST":
        file = request.files["file"]
        if file:
            filename = file.filename
            file.save(os.path.join("static/img", filename))
        return f"""
        <!doctype html>

    <head>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Варианты выбора</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

    </head>
        <html lang="en">
    <body>
    <link rel="stylesheet" href="../static/css/style.css">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
        
        <h2>Загрузка фотографии для участия в миссии.</h2>
        <form class="photo" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="photo">Выберите файл</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <button type="submit" class="btn btn-primary">Отправить</button>
            <img src='./static/img/{filename}'>
        </form>
        
            </body>
        </html>
"""


@app.route("/image_mars")
def image_mars():
    return """
    <!doctype html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
        <link rel="stylesheet" href="./static/css/style.css">
        <title>Привет, Марс!</title>
    </head>
        <html lang="en">
        <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
        <h1 style="color: red;">Жди нас, Марс!</h1>
        <img src='./static/img/image_mars.png'>
        <p>Вот она какая, красная планета.</p>


        </body>
        </html>
        """


@app.route("/promotion_image")
def promotion_image():
    return """
    <!doctype html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
        <link rel="stylesheet" href="./static/css/style.css">
        <title>Привет, Марс!</title>
    </head>
        <html lang="en">
        <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
        <h1 style="color: red;">Жди нас, Марс!</h1>
        <img src='./static/img/image_mars.png'>
        <p class='p1'>Человечество вырастает из детства.</p>
        <p class='p2'>Человечеству мала одна планета.</p>
        <p class='p3'>Мы сделаем обитаемыми безжизненные пока планеты.</p>
        <p class='p4'>И начнем с Марса!</p>
        <p class='p5'>Присоединяйся!</p>


        </body>
        </html>
        """


@app.route("/astronaut_selection", methods=["POST", "GET"])
def form_sample():
    if request.method == "GET":
        return """
        <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <link rel="stylesheet" href="./static/css/style.css">
    <title>Анкета</title>
</head>
<body>
    <h1>Анкета участника</h1>
    <div>
        <form class="login_form" method="post">
            <input type="text" class="form-control" id="text" placeholder="Введите фамилию" name="text">
            <input type="text" class="form-control" id="text" placeholder="Введите имя" name="text">
            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
            <div class="form-group">
                <label for="classSelect">Ваше образование</label>
                <select class="form-control" id="classSelect" name="class">
                  <option>Начальное</option>
                  <option>Среднее</option>
                  <option>Высшее</option>
              </select>
          </div>
          <div>
            <label for="classSelect">Ваши профессии</label>
            <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
          </p>
          <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">пилот</label>
          </p>
          <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">строитель</label>
          </p>
          <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">экзобиолог</label>
          </p>
          <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">врач</label>
          </p>
          <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">инженер по терраформированию</label>
          </p>
          <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">гляциолог</label>
          </p>
          <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">оператор марсохода</label>
          </p>
          <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">киберинженер</label>
          </p>
          <p>
              <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
              <label class="form-check-label" for="acceptRules">штурман</label></p>
              <p><input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                  <label class="form-check-label" for="acceptRules">пилот дронов</label></p>
              </div>

              <div class="form-group">
                <label for="about">Почему вы хотите принять участие в миссии?</label>
                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
            </div>
            <div class="form-group">
                <label for="photo">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <div class="form-group">
                <label for="form-check">Укажите пол</label>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                  <label class="form-check-label" for="male">
                    Мужской
                </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
              <label class="form-check-label" for="female">
                Женский
            </label>
        </div>
    </div>
    <div class="form-group form-check">
        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
</div>
</body>
</html>


        """
    elif request.method == "POST":
        print(request.form["email"])
        print(request.form["text"])
        print(request.form["class"])
        print(request.form["file"])
        print(request.form["about"])
        print(request.form["accept"])
        print(request.form["sex"])
        return "Форма отправлена"


@app.route("/<title>")
def index(title):
    return render_template("index.html", title=title)


@app.route("/index")
def index2():
    user = "Ученик"
    return render_template("index2.html", title="Дом", username=user)


@app.route("/list_prof/<h>")
def profs(h):
    p = [
        "Врач",
        "Строитель",
        "Инженер",
        "Летчик",
        "Космонавт",
        "Испытатель",
        "Пилот",
        "Повар",
        "Механик",
    ]
    return render_template("list_prof.html", h=h, p=p)


@app.route("/training/<prof>")
def training(prof):
    header = (
        "Инженерные тренажеры"
        if ("инженер" in prof or "строитель" in prof)
        else "Научные симуляторы"
    )
    return render_template("training.html", header=header, prof=prof)



@app.route('/galery', methods=['POST', 'GET'])
def galery():
  global photos
  return render_template("galery.html", photos=photos)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
  global photos
  file = request.files["file"]
  if file:
      filename = file.filename
      file.save(os.path.join("static/img", filename))
  photos.append(file.filename)
  
  return redirect('/galery')