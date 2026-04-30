import os
from flask import Flask, request
from greetings import get_greeting, get_time_based_greeting

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "World")
    lang = request.args.get("lang", "en")
    time_aware = request.args.get("time_aware", "false").lower() == "true"
    if time_aware:
        message = get_time_based_greeting(name)
    else:
        message = get_greeting(name, lang)
    return f"""<!DOCTYPE html>
<html>
<head>
  <title>Hello World Python</title>
  <style>
    body {{ font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; background: #f0f4f8; }}
    h1 {{ font-size: 3rem; color: #2d3748; }}
    p {{ color: #718096; font-size: 1rem; }}
    a {{ color: #4299e1; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <h1>{message}</h1>
  <p>Try:
    <a href="/?name=Andrei&lang=ro">/?name=Andrei&lang=ro</a> &nbsp;|&nbsp;
    <a href="/?name=World&lang=es">/?name=World&lang=es</a> &nbsp;|&nbsp;
    <a href="/?time_aware=true">/?time_aware=true</a>
  </p>
</body>
</html>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
