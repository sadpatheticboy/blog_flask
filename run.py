from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='Главная страница')


@app.route('/python_page')
def python_page():
    return render_template('python_page.html')


@app.route('/algorithms_page')
def algorithms_page():
    return render_template('algorithms_page.html')


@app.route('/flask_page')
def flask_page():
    return render_template('flask_page.html')


@app.route('/sql_page')
def sql_page():
    return render_template('sql_page.html')


@app.route('/css_page')
def css_page():
    return render_template('css_page.html')


@app.route('/html_page')
def html_page():
    return render_template('html_page.html')


if __name__ == '__main__':
    app.run(debug=True)
