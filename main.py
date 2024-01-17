"""Entrypoint script for interactive terminal of jciphers."""
from jcipherclasses import (
    CaesarShiftCipher,
    MlecchitaVikaalpaRomanCipher,
    RailFenceCipher,
    VigenereCipher,
)
from util import option_selection, terminal_clear


def display_substitution_ciphers():
    continue_index = None
    while continue_index is None or continue_index == 0:
        terminal_clear()
        print(
            """====================
Substitution Ciphers
====================
"""
        )
        choice_index = option_selection(
            prompt="Choose a substitution cipher:",
            options=["Caesar Shift", "Mlecchita Vikaalpa (Roman)", "Vigenère", "Quit"],
        )
        cipher = None
        if choice_index == 0:
            cipher = CaesarShiftCipher()
        elif choice_index == 1:
            cipher = MlecchitaVikaalpaRomanCipher()
        elif choice_index == 2:
            cipher = VigenereCipher()
        elif choice_index == 3:
            return
        cipher.intro()
        cipher.core_loop()
        continue_index = option_selection(
            "\nContinue using substitution ciphers?", ["Yes", "No"]
        )
        if continue_index == 1:
            return


def display_transposition_ciphers() -> None:
    continue_index = None
    while continue_index is None or continue_index == 0:
        terminal_clear()
        print(
            """=====================
Transposition Ciphers
=====================
"""
        )
        choice_index = option_selection(
            prompt="Choose a transposition cipher:", options=["Rail Fence", "Quit"]
        )
        cipher = None
        if choice_index == 0:
            cipher = RailFenceCipher()
        elif choice_index == 1:
            return
        cipher.intro()
        cipher.core_loop()
        continue_index = option_selection(
            "\nContinue using transposition ciphers?", ["Yes", "No"]
        )
        if continue_index == 1:
            return


def main():
    """Main process."""
    choice_index = None
    while choice_index != 2:
        terminal_clear()
        print(
            """========
jciphers
========

Inspired by the work of Simon Singh in his book "The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Crytography".

* Coded by Jonathan Ferreira.
* Ciphers developed by a ton of ancient and modern peoples.
            """
        )
        choice_index = option_selection(
            prompt="\nChoose a cipher type.",
            options=["Transposition", "Substitution", "Quit"],
        )
        if choice_index == 0:
            display_transposition_ciphers()
        elif choice_index == 1:
            display_substitution_ciphers()


if __name__ == "__main__":
    main()
