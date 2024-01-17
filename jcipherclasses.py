"""jciphers classes for displaying and running cipher functions in an interactive terminal."""
from dataclasses import dataclass

from jciphers.helper import (
    UnsupportedKeyError,
    UnsupportedMessageError,
    format_cipher_string,
)
from jciphers.substitution import (
    decrypt_caesar_shift,
    decrypt_general_substitution_with_key,
    decrypt_mlecchita_vikaalpa_roman,
    decrypt_vigenere,
    encrypt_caesar_shift,
    encrypt_general_substitution_with_key,
    encrypt_mlecchita_vikaalpa_roman,
    encrypt_vigenere,
)
from jciphers.transposition import decrypt_rail_fence, encrypt_rail_fence
from util import option_selection, terminal_clear, validate_key, validate_message

__all__ = [
    "CaesarShiftCipher",
    "MlecchitaVikaalpaRomanCipher",
    "RailFenceCipher",
    "VigenereCipher",
]


@dataclass
class CaesarShiftCipherMessage:
    message: str
    shifts: int


@dataclass
class MlecchitaVikaalpaRomanCipherMessage:
    message: str
    cipher_alphabet: str


@dataclass
class RailFenceCipherMessage:
    message: str
    levels: int


@dataclass
class VigenereCipherMessage:
    message: str
    key: str


class CaesarShiftCipher:
    def __init__(self):
        self.last_fifteen_messages = []

    def cache_message(self, message: str, shifts: int) -> None:
        len_messages = len(self.last_fifteen_messages)
        if len_messages == 15:
            self.last_fifteen_messages.pop(len_messages - 1)
        self.last_fifteen_messages.insert(0, CaesarShiftCipherMessage(message, shifts))

    def core_loop(self):
        continue_index = None
        while continue_index is None or continue_index == 0:
            try:
                choice_index = self.prompt_cipher_functions()
                if choice_index == 0:
                    self.encrypt()
                elif choice_index == 1:
                    self.decrypt()
                elif choice_index == 2:
                    self.display_last_fifteen_messages()
                elif choice_index == 3:
                    return
                continue_index = option_selection(
                    "\nContinue using Caesar shift ciphers?", ["Yes", "No"]
                )
                if continue_index == 1:
                    return
                terminal_clear()
                self.intro()
            except (UnsupportedKeyError, UnsupportedMessageError):
                continue

    def decrypt(self) -> str:
        # TODO: Format input message, removing spaces, punctuation, and unsupported characters.
        # TODO: Ask the user if we can remove unsupported characters or prompt for re-entry.
        message = input("\nEnter a message to decrypt: ")
        validate_message(message)
        message = format_cipher_string(message)
        validate_message(message)
        shifts = self.prompt_shifts()
        decrypted_message = decrypt_caesar_shift(message, shifts)
        self.cache_message(decrypted_message, shifts)
        print(f"Your decrypted message is: {decrypted_message}")

    def display_last_fifteen_messages(self) -> None:
        print("#. MESSAGE | SHIFTS")
        if len(self.last_fifteen_messages) == 0:
            print("No entries.")
        for index, message in enumerate(self.last_fifteen_messages):
            print(f"{index + 1}. {message.message} | {message.shifts}")

    def encrypt(self) -> str:
        # TODO: Format input message, removing spaces, punctuation, and unsupported characters.
        # TODO: Ask the user if we can remove unsupported characters or prompt for re-entry.
        message = input("\nEnter a message to encrypt: ")
        validate_message(message)
        message = format_cipher_string(message)
        validate_message(message)
        shifts = self.prompt_shifts()
        encrypted_message = encrypt_caesar_shift(message, shifts)
        self.cache_message(encrypted_message, shifts)
        print(f"Your encrypted message is: {encrypted_message}")

    def intro(self):
        terminal_clear()
        # TODO: Explain Caesar shift ciphers.
        print(
            """===================
Caesar Shift Cipher
===================
"""
        )

    def prompt_cipher_functions(self) -> int:
        choice_index = option_selection(
            "Choose a function:",
            options=[
                "Encrypt Caesar shift",
                "Decrypt Caesar shift",
                "Display last fifteen results",
                "Quit",
            ],
        )
        return choice_index

    def prompt_shifts(self) -> int:
        # TODO: Explain shifts!
        shifts = None
        while shifts is None or shifts < 0 or shifts > 25:
            try:
                shifts = input("\nEnter number of cipher shifts (min: 1, max: 25): ")
                shifts = int(shifts)
            except ValueError:
                print("\nInvalid input. Must be a number.")
                shifts = None
        return shifts


class MlecchitaVikaalpaRomanCipher:
    def __init__(self):
        self.last_fifteen_messages = []

    def cache_message(self, message: str, cipher_alphabet: str) -> None:
        len_messages = len(self.last_fifteen_messages)
        if len_messages == 15:
            self.last_fifteen_messages.pop(len_messages - 1)
        self.last_fifteen_messages.insert(
            0, MlecchitaVikaalpaRomanCipherMessage(message, cipher_alphabet)
        )

    def core_loop(self):
        continue_index = None
        while continue_index is None or continue_index == 0:
            try:
                choice_index = self.prompt_cipher_functions()
                if choice_index == 0:
                    self.encrypt()
                elif choice_index == 1:
                    self.decrypt()
                elif choice_index == 2:
                    self.display_last_fifteen_messages()
                elif choice_index == 3:
                    return
                continue_index = option_selection(
                    "\nContinue using Mlecchita Vikaalpa ciphers?", ["Yes", "No"]
                )
                if continue_index == 1:
                    return
                terminal_clear()
                self.intro()
            except (UnsupportedKeyError, UnsupportedMessageError):
                continue

    def decrypt(self) -> str:
        # TODO: Format input message, removing spaces, punctuation, and unsupported characters.
        # TODO: Ask the user if we can remove unsupported characters or prompt for re-entry.
        message = input("\nEnter a message to decrypt: ")
        validate_message(message)
        message = format_cipher_string(message)
        cipher_alphabet = input("\nEnter the cipher alphabet: ")
        validate_key(cipher_alphabet)
        decrypted_message = decrypt_mlecchita_vikaalpa_roman(message, cipher_alphabet)
        self.cache_message(decrypted_message, cipher_alphabet)
        print(f"Your decrypted message is: {decrypted_message}")

    def display_last_fifteen_messages(self) -> None:
        print("#. MESSAGE")
        if len(self.last_fifteen_messages) == 0:
            print("No entries.")
        for index, message in enumerate(self.last_fifteen_messages):
            print(f"{index + 1}. {message.message}")

    def encrypt(self) -> str:
        # TODO: Format input message, removing spaces, punctuation, and unsupported characters.
        # TODO: Ask the user if we can remove unsupported characters or prompt for re-entry.
        message = input("\nEnter a message to encrypt: ")
        validate_message(message)
        message = format_cipher_string(message)
        encrypted_message, cipher_alphabet = encrypt_mlecchita_vikaalpa_roman(message)
        self.cache_message(encrypted_message, cipher_alphabet)
        print(f"Generated cipher alphabet: {cipher_alphabet}")
        print(f"Your encrypted message is: {encrypted_message}")

    def intro(self):
        terminal_clear()
        # TODO: Explain Mlecchita Vikaalpa ciphers.
        print(
            """=========================
Mlecchita Vikaalpa Cipher
=========================
"""
        )

    def prompt_cipher_functions(self) -> int:
        choice_index = option_selection(
            "Choose a function:",
            options=[
                "Encrypt Mlecchita Vikaalpa (Roman)",
                "Decrypt Mlecchita Vikaalpa (Roman)",
                "Display last fifteen results",
                "Quit",
            ],
        )
        return choice_index


class RailFenceCipher:
    def __init__(self):
        self.last_fifteen_messages = []

    def cache_message(self, message: str, levels: int) -> None:
        len_messages = len(self.last_fifteen_messages)
        if len_messages == 15:
            self.last_fifteen_messages.pop(len_messages - 1)
        self.last_fifteen_messages.insert(0, RailFenceCipherMessage(message, levels))

    def core_loop(self):
        continue_index = None
        while continue_index is None or continue_index == 0:
            try:
                choice_index = self.prompt_cipher_functions()
                if choice_index == 0:
                    self.encrypt()
                elif choice_index == 1:
                    self.decrypt()
                elif choice_index == 2:
                    self.display_last_fifteen_messages()
                elif choice_index == 3:
                    return
                continue_index = option_selection(
                    "\nContinue using rail ciphers?", ["Yes", "No"]
                )
                if continue_index == 1:
                    return
                terminal_clear()
                self.intro()
            except (UnsupportedKeyError, UnsupportedMessageError):
                continue

    def decrypt(self) -> str:
        # TODO: Format input message, removing spaces, punctuation, and unsupported characters.
        # TODO: Ask the user if we can remove unsupported characters or prompt for re-entry.
        message = input("\nEnter a message to decrypt: ")
        validate_message(message)
        message = format_cipher_string(message)
        levels = self.prompt_levels()
        decrypted_message = decrypt_rail_fence(message, levels)
        self.cache_message(decrypted_message, levels)
        print(f"Your decrypted message is: {decrypted_message}")

    def display_last_fifteen_messages(self) -> None:
        print("#. MESSAGE | LEVELS")
        if len(self.last_fifteen_messages) == 0:
            print("No entries.")
        for index, message in enumerate(self.last_fifteen_messages):
            print(f"{index + 1}. {message.message} | {message.levels}")

    def encrypt(self) -> str:
        # TODO: Format input message, removing spaces, punctuation, and unsupported characters.
        # TODO: Ask the user if we can remove unsupported characters or prompt for re-entry.
        message = input("\nEnter a message to encrypt: ")
        validate_message(message)
        message = format_cipher_string(message)
        levels = self.prompt_levels()
        encrypted_message = encrypt_rail_fence(message, levels)
        self.cache_message(encrypted_message, levels)
        print(f"Your encrypted message is: {encrypted_message}")

    def intro(self):
        terminal_clear()
        # TODO: Explain rail fence ciphers.
        print(
            """=================
Rail Fence Cipher
=================
"""
        )

    def prompt_cipher_functions(self) -> int:
        choice_index = option_selection(
            "Choose a function:",
            options=[
                "Encrypt rail fence",
                "Decrypt rail fence",
                "Display last fifteen results",
                "Quit",
            ],
        )
        return choice_index

    def prompt_levels(self) -> int:
        # TODO: Explain levels!
        levels = None
        while levels is None or levels < 2 or levels > 99:
            try:
                levels = input(
                    "\nEnter number of transposition levels (min: 2, max: 99): "
                )
                levels = int(levels)
            except ValueError:
                print("\nInvalid input. Must be a number.")
                levels = None
        return levels


class VigenereCipher:
    def __init__(self):
        self.last_fifteen_messages = []

    def cache_message(self, message: str, key: str) -> None:
        len_messages = len(self.last_fifteen_messages)
        if len_messages == 15:
            self.last_fifteen_messages.pop(len_messages - 1)
        self.last_fifteen_messages.insert(0, VigenereCipherMessage(message, key))

    def core_loop(self):
        continue_index = None
        while continue_index is None or continue_index == 0:
            try:
                choice_index = self.prompt_cipher_functions()
                if choice_index == 0:
                    self.encrypt()
                elif choice_index == 1:
                    self.decrypt()
                elif choice_index == 2:
                    self.display_last_fifteen_messages()
                elif choice_index == 3:
                    return
                continue_index = option_selection(
                    "\nContinue using Vigenère ciphers?", ["Yes", "No"]
                )
                if continue_index == 1:
                    return
                terminal_clear()
                self.intro()
            except (UnsupportedKeyError, UnsupportedMessageError):
                continue

    def decrypt(self) -> str:
        # TODO: Format input message, removing spaces, punctuation, and unsupported characters.
        # TODO: Ask the user if we can remove unsupported characters or prompt for re-entry.
        message = input("\nEnter a message to decrypt: ")
        validate_message(message)
        message = format_cipher_string(message)
        key = input("\nEnter the cipher key: ")
        validate_key(key)
        key = format_cipher_string(key)
        decrypted_message = decrypt_vigenere(message, key)
        self.cache_message(decrypted_message, key)
        print(f"Your decrypted message is: {decrypted_message}")

    def display_last_fifteen_messages(self) -> None:
        print("#. MESSAGE | KEY")
        if len(self.last_fifteen_messages) == 0:
            print("No entries.")
        for index, message in enumerate(self.last_fifteen_messages):
            print(f"{index + 1}. {message.message} | {message.key}")

    def encrypt(self) -> str:
        # TODO: Format input message, removing spaces, punctuation, and unsupported characters.
        # TODO: Ask the user if we can remove unsupported characters or prompt for re-entry.
        message = input("\nEnter a message to encrypt: ")
        validate_message(message)
        message = format_cipher_string(message)
        key = input("\nEnter a cipher key: ")
        validate_key(key)
        key = format_cipher_string(key)
        encrypted_message = encrypt_vigenere(message, key)
        self.cache_message(encrypted_message, key)
        print(f"Your encrypted message is: {encrypted_message}")

    def intro(self):
        terminal_clear()
        # TODO: Explain Vigenere ciphers.
        print(
            """===============
Vigenère Cipher
===============
"""
        )

    def prompt_cipher_functions(self) -> int:
        choice_index = option_selection(
            "Choose a function:",
            options=[
                "Encrypt Vigenère",
                "Decrypt Vigenère",
                "Display last fifteen results",
                "Quit",
            ],
        )
        return choice_index
