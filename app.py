import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """<!DOCTYPE html>
<html>
<head>
  <title>I Love You</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #ff9a9e, #fecfef, #ffecd2);
      font-family: 'Pacifico', cursive;
      overflow: hidden;
    }
    .heart {
      font-size: 200px;
      animation: heartbeat 1.2s infinite ease-in-out;
      filter: drop-shadow(0 0 30px rgba(255, 50, 100, 0.6));
      line-height: 1;
    }
    @keyframes heartbeat {
      0%   { transform: scale(1); }
      14%  { transform: scale(1.15); }
      28%  { transform: scale(1); }
      42%  { transform: scale(1.1); }
      70%  { transform: scale(1); }
    }
    h1 {
      margin-top: 30px;
      font-size: 4rem;
      color: #c0114a;
      text-shadow: 3px 3px 0 rgba(255,255,255,0.5);
      letter-spacing: 2px;
    }
    .sparkles { position: fixed; width: 100%; height: 100%; pointer-events: none; top: 0; left: 0; }
    .sparkle { position: absolute; animation: float linear infinite; opacity: 0.7; }
    @keyframes float {
      0%   { transform: translateY(0) rotate(0deg); opacity: 0.7; }
      50%  { opacity: 1; }
      100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }
  </style>
</head>
<body>
  <div class="heart">&#10084;&#65039;</div>
  <h1>I Love You</h1>
  <div class="sparkles" id="sparkles"></div>
  <script>
    const emojis = ['\u{1F495}','\u{1F496}','\u{1F497}','\u{1F493}','\u{1F49E}','\u2728','\u{1F339}','\u{1F49D}'];
    const container = document.getElementById('sparkles');
    for (let i = 0; i < 20; i++) {
      const el = document.createElement('div');
      el.className = 'sparkle';
      el.textContent = emojis[Math.floor(Math.random() * emojis.length)];
      el.style.left = Math.random() * 100 + '%';
      el.style.top = Math.random() * 100 + '%';
      const dur = 4 + Math.random() * 6;
      el.style.animation = `float ${dur}s linear infinite`;
      el.style.animationDelay = -Math.random() * dur + 's';
      el.style.fontSize = (1 + Math.random() * 2) + 'rem';
      container.appendChild(el);
    }
  </script>
</body>
</html>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
