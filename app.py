from flask import Flask, render_template, request

# определение в каком режиме запустится сервер
DEBUG = True #запущено в режиме отладки
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST']) #точка входа на сайт
def index():
    return render_template('index.html') #возвращает шаблона index


@app.route('/handle_data', methods=['GET', 'POST']) #обработка запроса
def handle_data():
    projectpath = request.form['text'] #забираем число из формы

    hex_num = "" #переменная для результата операции
    #перевод числа из 10 в 16 систему счисления
    try: #отлов ошибок ввода
        decimal_num = int(projectpath) #переводим данные в 10 систему счисления
        hex_num = hex(decimal_num).upper()[2:] #переводим данные в 16 систему счисления и форматируем выводr
    except ValueError:
        hex_num = "Хорош нарушать гармонию не кошерными символами" #выводим в случае ошибки

    return render_template('index.html', hex_num=hex_num) #отдаем данные в шаблон индекс


if __name__ == '__main__': #контролирует правильно ли запущено приложение
    app.run()
