#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Return 0-index.html content"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
