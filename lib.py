"""Набір функцій для шифрування за алгоритмом Цезаря та обчислення степенів із перевіркою знаку."""

def caesar_cipher(text: str, shift: int = 3) -> str:
    """Шифрує текст за алгоритмом Цезаря для латиниці та кирилиці."""
    encrypted_chars = []

    for char in text:
        if "a" <= char <= "z":
            start = ord("a")
            encrypted_chars.append(chr((ord(char) - start + shift) % 26 + start))
        elif "A" <= char <= "Z":
            start = ord("A")
            encrypted_chars.append(chr((ord(char) - start + shift) % 26 + start))
        elif "а" <= char <= "я":
            start = ord("а")
            encrypted_chars.append(chr((ord(char) - start + shift) % 32 + start))
        elif "А" <= char <= "Я":
            start = ord("А")
            encrypted_chars.append(chr((ord(char) - start + shift) % 32 + start))
        else:
            encrypted_chars.append(char)

    return "".join(encrypted_chars)


def power_with_sign_check(base: int, exponent: int) -> dict:
    """Підносить число до степеня та визначає знак результату."""
    result = base**exponent
    absolute_value = abs(result)

    if result > 0:
        sign = "додатне"
    elif result < 0:
        sign = "від'ємне"
    else:
        sign = "нуль"

    return {
        "base": base,
        "exponent": exponent,
        "result": result,
        "abs_result": absolute_value,
        "sign": sign,
    }