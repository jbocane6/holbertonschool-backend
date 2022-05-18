#!/usr/bin/env python3
"""
First you will setup a basic Flask app in 0-app.py.
Creates a single / route and an index.html template
that simply outputs “Welcome to Holberton” as page title(<title>)
and “Hello world” as header (<h1>).
"""


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Has LANGUAGES class attributes.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def test_page():
    """
    Creates a single / route and an index.html template.
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    Get locale from request.
    """
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
