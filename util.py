"""Utility module for interactive terminal of jciphers."""
import os
import string

__all__ = [
    "option_selection",
    "terminal_clear",
    "validate_message",
]
from jciphers.helper import UnsupportedKeyError, UnsupportedMessageError


def option_selection(prompt: str, options: list) -> int:
    selection = prompt + "\n"
    for index, choice in enumerate(options):
        selection += f"({index + 1}) {choice}\n"
    selection += "\n> "
    choice_index = None
    while choice_index is None or choice_index < 1 or choice_index > len(options):
        choice_index = input(selection)
        try:
            choice_index = int(choice_index)
        except ValueError:
            print("\nInvalid input. Must be a number.")
            choice_index = None
    return choice_index - 1


def terminal_clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def validate_key(key: str) -> None:
    for char in key:
        if char == string.whitespace:
            continue
        if char in string.punctuation:
            continue
        if char in string.digits:
            print("Numbers are not supported in your key.")
            raise UnsupportedKeyError()
        upper_char_ord = ord(char.upper())
        if upper_char_ord < 65 or upper_char_ord > 90:
            print(
                f"Unsupported character in key: {char}. Only Latin characters are supported at this time."
            )
            raise UnsupportedKeyError()


def validate_message(message: str) -> None:
    for char in message:
        if char == " ":
            continue
        if char in string.punctuation:
            continue
        if char in string.digits:
            print("Numbers are not supported in your message.")
            raise UnsupportedMessageError()
        upper_char_ord = ord(char.upper())
        if upper_char_ord < 65 or upper_char_ord > 90:
            print(
                f"Unsupported character in message: {char}. Only Latin characters are supported at this time."
            )
            raise UnsupportedMessageError()
