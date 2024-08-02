from flask import Flask
from flask import render_template, url_for, redirect, request
import requests as rq

app = Flask(__name__)


@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/home")
def home():
    return render_template('index.html')

if __name__ == "__main__":
        app.run(debug=True)