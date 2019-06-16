import os

from flask import Flask, jsonify, render_template


class ProductionConfig:
    DEBUG = False


class DevelopmentConfig:
    DEBUG = True
    JSON_AS_ASCII = False


app = Flask(__name__)
mode = os.environ['MODE']

if mode == 'Production':
    app.config.from_object(ProductionConfig)
elif mode == 'Development':
    app.config.from_object(DevelopmentConfig)
else:
    raise Exception("You have to set environment variable `MODE=Development`")


@app.route("/json")
def json_api():
    return jsonify(dict(status=200, messge='Hello, world'))


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
