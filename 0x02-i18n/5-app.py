#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict

class Config:
    """Config Class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages"""

    lang = request.args.get('locale')

    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Dict:
    """Returns a user dictionary or None if the ID cannot be found"""
    login_id = request.get.args('login_as')
    return users.get(login_id, None)


@app.before_request
def before_request() -> None:
    """use get_user to find a user if any"""
    user = get_user()
    g.user = user


@app.route('/')
def home():
    """Return 0-index.html content"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
