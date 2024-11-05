#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config Class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def home():
    """Return 0-index.html content"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
