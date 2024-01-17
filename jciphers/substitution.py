"""Substitution ciphers."""
import random
import string

from jciphers.helper import format_cipher_string

__all__ = [
    "decrypt_caesar_shift",
    "decrypt_general_substitution_with_key",
    "decrypt_mlecchita_vikaalpa_roman",
    "decrypt_vigenere",
    "encrypt_caesar_shift",
    "encrypt_general_substitution_with_key",
    "encrypt_mlecchita_vikaalpa_roman",
    "encrypt_vigenere",
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


def decrypt_caesar_shift(encrypted_message: str, shifts: int) -> str:
    if shifts < 1 or shifts > 25:
        raise IndexError(
            "A Caesar shift cipher requires at least 1 shift or at most 25 shifts."
        )
    encrypted_message = format_cipher_string(encrypted_message)
    decrypted_message = ""
    for char in encrypted_message:
        ordinal = ord(char)
        if ordinal - shifts < 65:
            ordinal += 26
        decrypted_message += chr(ordinal - shifts)
    return decrypted_message


def decrypt_general_substitution_with_key(message: str, key: str) -> str:
    message = format_cipher_string(message)
    key = format_cipher_string(key)
    cipher_key = _build_caesar_cipher_key(key)
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(cipher_key.index(char) + 65)
    return encrypted_message


def decrypt_mlecchita_vikaalpa_roman(
    encrypted_message: str, cipher_alphabet: str
) -> str:
    encrypted_message = format_cipher_string(encrypted_message)
    cipher_alphabet = list(cipher_alphabet)
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(cipher_alphabet.index(char) + 65)
    return decrypted_message


def decrypt_mlecchita_vikaalpa_roman_default_cipher(encrypted_message: str) -> str:
    encrypted_message = format_cipher_string(encrypted_message)
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += _mlecchita_vikaalpa_roman_cipher[char]
    return decrypted_message


def decrypt_vigenere(message: str, key: str) -> str:
    message = format_cipher_string(message)
    key = format_cipher_string(key)
    key_index = 0
    encrypted_message = ""
    for char in message:
        ordinal = ord(char)
        key_ordinal = ord(key[key_index]) + 1 - 65
        if ordinal - key_ordinal < 65:
            ordinal += 26
        encrypted_message += chr(ordinal - key_ordinal)
        key_index += 1
        if key_index == len(key):
            key_index = 0
    return encrypted_message


def encrypt_caesar_shift(message: str, shifts: int) -> str:
    if shifts < 1 or shifts > 25:
        raise IndexError(
            "A Caesar shift cipher requires at least 1 shift or at most 25 shifts."
        )
    message = format_cipher_string(message)
    encrypted_message = ""
    for char in message:
        ordinal = ord(char)
        if ordinal + shifts > 90:
            ordinal -= 26
        encrypted_message += chr(ordinal + shifts)
    return encrypted_message


def encrypt_general_substitution_with_key(message: str, key: str) -> str:
    message = format_cipher_string(message)
    key = format_cipher_string(key)
    cipher_key = _build_caesar_cipher_key(key)
    encrypted_message = ""
    for char in message:
        encrypted_message += cipher_key[ord(char) - 65]
    return encrypted_message


def encrypt_mlecchita_vikaalpa_roman(message: str) -> tuple[str, str]:
    message = format_cipher_string(message)
    cipher_alphabet = list(string.ascii_uppercase)
    random.shuffle(cipher_alphabet)
    encrypted_message = ""
    for char in message:
        encrypted_message += cipher_alphabet[ord(char) - 65]
    return encrypted_message, "".join(cipher_alphabet)


def encrypt_mlecchita_vikaalpa_roman_default_cipher(message: str) -> str:
    message = format_cipher_string(message)
    encrypted_message = ""
    for char in message:
        encrypted_message += _mlecchita_vikaalpa_roman_cipher[char]
    return encrypted_message


def encrypt_vigenere(message: str, key: str) -> str:
    message = format_cipher_string(message)
    key = format_cipher_string(key)
    key_index = 0
    encrypted_message = ""
    for char in message:
        ordinal = ord(char)
        key_ordinal = ord(key[key_index]) + 1 - 65
        if ordinal + key_ordinal > 90:
            ordinal -= 26
        encrypted_message += chr(ordinal + key_ordinal)
        key_index += 1
        if key_index == len(key):
            key_index = 0
    return encrypted_message


def _build_caesar_cipher_key(key: str) -> str:
    """Builds a Caesar cipher using a key."""
    cipher_key = [0] * 26
    cipher_key_len = 0
    last_ord = None
    for char in key:
        if char not in cipher_key:
            cipher_key[cipher_key_len] = char
            last_ord = ord(char)
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
