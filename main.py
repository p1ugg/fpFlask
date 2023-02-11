from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def f():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    my_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
               'Мы сделаем обитаемыми безжизненные пока планеты.',
               'И начнем с Марса!', 'Присоединяйся!']
    return '<br>'.join(my_list)


@app.route('/promotion_image')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Жди нас, Илон</h1>
                    <img src="{url_for('static', filename='img/mars.png')}">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастет из детства  
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-info" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
