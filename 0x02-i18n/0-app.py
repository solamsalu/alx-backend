#!/usr/bin/env python3
""" Task 0: Basic Flask app """

from flask import Flask, render_template
app = Flask(name)


@app.route('/')
def index():
    return render_template('index.html')
