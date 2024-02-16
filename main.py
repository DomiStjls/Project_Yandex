from flask import Flask, request, url_for

app = Flask(__name__)


@app.route("/")
def base():
    return "Миссия Колонизация Марса!"


@app.route("/choice/<planet_name>")
def index(planet_name):
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


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
