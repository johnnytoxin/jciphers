"""Transposition ciphers."""

__all__ = ["decrypt_rail_fence", "encrypt_rail_fence"]


def decrypt_rail_fence(encrypted_message: str, levels: int) -> str:
    """Decrypts a message encoded with a rail fence transposition."""
    encrypted_message = encrypted_message.replace(" ", "")
    array = [0] * len(encrypted_message)
    index = 0
    index_offset = 0
    for char in encrypted_message:
        array[index + index_offset] = char
        index += levels
        if index + index_offset >= len(encrypted_message):
            index = 0
            index_offset += 1
    return "".join(array)


def encrypt_rail_fence(message: str, levels: int) -> str:
    """Transposes letters of a message in an alternating fashion using n alternate lines."""
    message = message.replace(" ", "")
    arrays = []
    for _ in range(levels):
        arrays.append([])
    index = 0
    for char in message:
        arrays[index].append(char.upper())
        index = index + 1 if index + 1 < levels else 0
    joined_arrays = []
    for array in arrays:
        joined_arrays += array
    return "".join(joined_arrays)
