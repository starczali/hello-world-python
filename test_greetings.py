from datetime import datetime

from greetings import get_greeting, get_time_based_greeting


def test_default_greeting_english():
    assert get_greeting("World", "en") == "Hello, World!"


def test_romanian_greeting():
    assert get_greeting("Andrei", "ro") == "Salut, Andrei!"


def test_unknown_language_falls_back_to_english():
    assert get_greeting("Sam", "jp") == "Hello, Sam!"


def test_morning_time_based_greeting():
    morning = datetime(2026, 4, 30, 8, 0, 0)
    assert get_time_based_greeting("Andrei", now=morning) == "Good morning, Andrei!"


def test_evening_time_based_greeting():
    evening = datetime(2026, 4, 30, 19, 0, 0)
    assert get_time_based_greeting("Andrei", now=evening) == "Good evening, Andrei!"
