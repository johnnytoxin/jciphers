"""Substitution ciphers."""

__all__ = [
    "decrypt_caesar_shift",
    "decrypt_caesar_shift_with_key",
    "decrypt_mlecchita_vikaalpa_roman",
    "encrypt_caesar_shift",
    "encrypt_caesar_shift_with_key",
    "encrypt_mlecchita_vikaalpa_roman",
]

_mlecchita_vikaalpa_roman_cipher = {
    "A": "V",
    "B": "H",
    "C": "M",
    "D": "X",
    "E": "U",
    "F": "W",
    "G": "I",
    "H": "B",
    "I": "G",
    "J": "K",
    "K": "J",
    "L": "R",
    "M": "C",
    "N": "S",
    "O": "Q",
    "P": "Y",
    "Q": "O",
    "R": "L",
    "S": "N",
    "T": "Z",
    "U": "E",
    "V": "A",
    "W": "F",
    "X": "D",
    "Y": "P",
    "Z": "T",
}


def decrypt_caesar_shift(encrypted_message: str, places: int) -> str:
    if places < 1 or places > 25:
        raise IndexError(
            "A Caesar shift cipher requires at least 1 place or at most 25 places."
        )
    decrypted_message = ""
    for char in encrypted_message:
        ordinal = ord(char.upper())
        if ordinal - places < 65:
            ordinal += 26
        decrypted_message += chr(ordinal - places)
    return decrypted_message


def decrypt_caesar_shift_with_key(message: str, key: str) -> str:
    message = message.replace(" ", "")
    key = key.replace(" ", "")
    cipher_key = _build_caesar_cipher_key(key)
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(cipher_key.index(char.upper()) + 65)
    return encrypted_message


def decrypt_mlecchita_vikaalpa_roman(encrypted_message: str) -> str:
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += _mlecchita_vikaalpa_roman_cipher[char.upper()]
    return decrypted_message


def encrypt_caesar_shift(message: str, places: int) -> str:
    if places < 1 or places > 25:
        raise IndexError(
            "A Caesar shift cipher requires at least 1 place or at most 25 places."
        )
    message = message.replace(" ", "")
    encrypted_message = ""
    for char in message:
        ordinal = ord(char.upper())
        if ordinal + places > 90:
            ordinal -= 26
        encrypted_message += chr(ordinal + places)
    return encrypted_message


def encrypt_caesar_shift_with_key(message: str, key: str) -> str:
    message = message.replace(" ", "")
    key = key.replace(" ", "")
    cipher_key = _build_caesar_cipher_key(key)
    encrypted_message = ""
    for char in message:
        encrypted_message += cipher_key[ord(char.upper()) - 65]
    return encrypted_message


def encrypt_mlecchita_vikaalpa_roman(message: str) -> str:
    message = message.replace(" ", "")
    encrypted_message = ""
    for char in message:
        encrypted_message += _mlecchita_vikaalpa_roman_cipher[char.upper()]
    return encrypted_message


def _build_caesar_cipher_key(key: str) -> str:
    """Builds a Caesar cipher using a key."""
    cipher_key = [0] * 26
    cipher_key_len = 0
    last_ord = None
    for char in key:
        upper_char = char.upper()
        if upper_char not in cipher_key:
            cipher_key[cipher_key_len] = upper_char
            last_ord = ord(upper_char)
            cipher_key_len += 1
    last_ord += 1
    # TODO: Protect against clowns using the whole alphabet
    for i in range(26 - cipher_key_len):
        cipher_key[cipher_key_len + i] = chr(last_ord)
        last_ord += 1
        if last_ord > 90:
            last_ord -= 26
        while chr(last_ord) in cipher_key:
            last_ord += 1
    return cipher_key
