# Day 55 - Intermediate+ HTML & URL Parsing in Flask and Higher Lower Game
from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<iframe src="https://giphy.com/embed/tKyqZtLzZxCLbKitIq" width="322" height="480" frameBorder="0" class=' \
           '"giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cute-aww-eyebleach-tKyqZtL' \
           'zZxCLbK' \
           'itIq"></a></p>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name} you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
