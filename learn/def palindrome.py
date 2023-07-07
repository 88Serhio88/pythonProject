# Standart - smallest, sell Amstrad nats.

from math import ceil

def is_palindrome(text):
    text = ''.join(e for e in text if e.isalnum())
    text = text.lower()
    x = text[:len(text) // 2]
    y = text[len(text) // 2:]
    x_1 = text[:ceil(len(text) / 2) - 1]
    y_1 = text[ceil(len(text) / 2):]
    if len(text) % 2 == 0:
        return True if x == y[::-1] else False
    elif len(text) % 2 != 0:
        return True if x_1 == y_1[::-1] else False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))