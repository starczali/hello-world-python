import json
import os
from datetime import date

from flask import Flask, jsonify, render_template, request

from greetings import get_greeting

app = Flask(__name__)


def calculate_age(birthdate):
    if not birthdate:
        return None
    try:
        bd = date.fromisoformat(birthdate)
    except ValueError:
        return None
    today = date.today()
    return today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))


def load_family():
    with open(os.path.join(app.root_path, "family.json"), encoding="utf-8") as f:
        people = json.load(f)["people"]
    for p in people:
        p["age"] = calculate_age(p.get("birthdate"))
    return people


@app.get("/")
def index():
    return render_template("index.html", message="I love you")


@app.get("/family")
def family():
    return render_template("family.html", people=load_family())


@app.get("/greet")
def greet():
    name = request.args.get("name", "World")
    lang = request.args.get("lang", "en")
    return jsonify(greeting=get_greeting(name, lang), name=name, lang=lang)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
