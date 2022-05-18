#!/usr/bin/env python3
"""
First you will setup a basic Flask app in 0-app.py.
Creates a single / route and an index.html template
that simply outputs “Welcome to Holberton” as page title(<title>)
and “Hello world” as header (<h1>).
"""


from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def test_page():
    """
    Creates a single / route and an index.html template.
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """
    Get locale from request.
    """
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(login_as):
    """
    Returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed.
    """
    try:
        return users.get(int(login_as))
    except Exception:
        return


@app.before_request
def before_request():
    """
    Should use get_user to find a user if any,
    and set it as a global on flask.g.user.
    """
    g.user = get_user(request.args.get("login_as"))


if __name__ == "__main__":
    app.run(debug=True)
