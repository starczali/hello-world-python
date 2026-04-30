from flask import Flask, jsonify, render_template, request

from greetings import get_greeting

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", message="I love you")


@app.get("/greet")
def greet():
    name = request.args.get("name", "World")
    lang = request.args.get("lang", "en")
    return jsonify(greeting=get_greeting(name, lang), name=name, lang=lang)


if __name__ == "__main__":
    app.run(debug=True)
