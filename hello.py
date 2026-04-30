import argparse

from greetings import get_greeting, get_time_based_greeting


def main():
    parser = argparse.ArgumentParser(description="Hello world CLI in multiple languages.")
    parser.add_argument("--name", default="World", help="Name to greet (default: World)")
    parser.add_argument(
        "--lang",
        default="en",
        choices=["en", "es", "fr", "ro", "de"],
        help="Greeting language (default: en)",
    )
    parser.add_argument(
        "--time-aware",
        action="store_true",
        help="Use a time-of-day greeting instead of the language greeting",
    )
    args = parser.parse_args()

    if args.time_aware:
        print(get_time_based_greeting(args.name))
    else:
        print(get_greeting(args.name, args.lang))


if __name__ == "__main__":
    main()
