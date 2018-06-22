import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/input')
def input():
    return render_template("input.html")

@app.route('/table')
def table():
    return render_template("table.html")

if __name__ == '__main__':
    app.run()
