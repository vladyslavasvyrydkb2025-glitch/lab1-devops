"""Головний модуль запуску програми."""

from lib import caesar_cipher, power_with_sign_check


def main():

    security_manifesto = (
        "Cybersecurity is not just about firewalls; it is an active defense. "
        "Every endpoint, encrypted packet, and access control policy shapes "
        "the resilience of digital infrastructure against zero-day threats."
    )

    shift = 23
    encrypted_text = caesar_cipher(security_manifesto, shift=shift)

    print("1. КРИПТОГРАФІЧНИЙ БЛОК (ШИФР ЦЕЗАРЯ)")
    print(f"Початковий текст: {security_manifesto}")
    print(f"Зсув шифру: {shift}")
    print(f"Зашифрований текст: {encrypted_text}\n")

    print("2. МАТЕМАТИЧНИЙ БЛОК (ПІДНЕСЕННЯ ДО СТЕПЕНЯ ТА АНАЛІЗ ЗНАКУ)")

    test_cases = [(-3, 3), (-2, 4), (5, 3)]

    for base, exp in test_cases:
        res = power_with_sign_check(base, exp)
        print(f"Число {res['base']} у степені {res['exponent']}:")
        print(f"  Результат: {res['result']}")
        print(f"  За модулем: {res['abs_result']}")
        print(f"  Знак: {res['sign']}")


if __name__ == "__main__":
    main()