"""Helper functions."""

__all__ = [
    "UnsupportedKeyError",
    "UnsupportedMessageError",
    "format_cipher_string",
]


class UnsupportedKeyError(Exception):
    """Unsupported key format received."""


class UnsupportedMessageError(Exception):
    """Unsupported message format received."""


def format_cipher_string(message: str) -> str:
    return message.replace(" ", "").upper()
