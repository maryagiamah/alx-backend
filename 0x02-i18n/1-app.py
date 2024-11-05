#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """Return 0-index.html content"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
