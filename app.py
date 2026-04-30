from flask import Flask, jsonify, request

from greetings import get_greeting

app = Flask(__name__)


@app.get("/greet")
def greet():
    name = request.args.get("name", "World")
    lang = request.args.get("lang", "en")
    return jsonify(greeting=get_greeting(name, lang), name=name, lang=lang)


if __name__ == "__main__":
    app.run(debug=True)
