import hmac
import json
import os
import secrets
from datetime import date
from functools import wraps

from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from greetings import get_greeting

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

APP_USERNAME = os.environ.get("APP_USERNAME", "tarczali")
APP_PASSWORD = os.environ.get("APP_PASSWORD", "saffron-crimson-breeze-harbor-84")


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)

    return wrapped


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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if hmac.compare_digest(username, APP_USERNAME) and hmac.compare_digest(
            password, APP_PASSWORD
        ):
            session["logged_in"] = True
            next_url = request.args.get("next") or url_for("index")
            return redirect(next_url)
        return (
            render_template("login.html", error="Invalid username or password"),
            401,
        )
    return render_template("login.html", error=None)


@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.get("/")
@login_required
def index():
    return render_template("index.html", message="I love you")


@app.get("/family")
@login_required
def family():
    return render_template("family.html", people=load_family())


@app.get("/greet")
@login_required
def greet():
    name = request.args.get("name", "World")
    lang = request.args.get("lang", "en")
    return jsonify(greeting=get_greeting(name, lang), name=name, lang=lang)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
