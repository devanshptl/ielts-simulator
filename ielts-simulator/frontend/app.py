from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

BACKEND_URL = "http://localhost:8000/api"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/part1")
def get_part1():
    response = requests.get(f"{BACKEND_URL}/part1/random/")
    return jsonify(response.json())


@app.route("/api/part2")
def get_part2():
    response = requests.get(f"{BACKEND_URL}/part2/random/")
    return jsonify(response.json())


@app.route("/api/part3")
def get_part3():
    response = requests.get(f"{BACKEND_URL}/part3/random/")
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
