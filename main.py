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


@app.route('/image_mars')
def image_mars():
    return '<br>'.join(['Жди нас, Илон Маск', f'''<img src="{url_for('static', filename='img/mars.png')}">'''])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
