from datetime import datetime

GREETINGS = {
    "en": "Hello",
    "es": "Hola",
    "fr": "Bonjour",
    "ro": "Salut",
    "de": "Hallo",
}


def get_greeting(name, lang):
    word = GREETINGS.get(lang, GREETINGS["en"])
    return f"{word}, {name}!"


def get_time_based_greeting(name, now=None):
    if now is None:
        now = datetime.now()
    hour = now.hour
    if 5 <= hour < 12:
        period = "morning"
    elif 12 <= hour < 18:
        period = "afternoon"
    elif 18 <= hour < 22:
        period = "evening"
    else:
        period = "night"
    return f"Good {period}, {name}!"
