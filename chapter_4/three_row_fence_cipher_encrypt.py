"""Шифровка текста трёхрядным зигзагообразным шрифтом
времён гражданской войны США. При шифровке пробелы (не?)будут утеряны.

Цели:
Три ряда вместо двух +
Сохранять пробелы +
Сохранять знаки препинания -"""

import random

#----------------------------------------------------------------------------
#ВХОДНЫЕ ДАННЫЕ:
plaintext = """Давай пересечём реку и отдохнём в тени деревьев"""
DEBUG = True
#КОНЕЦ ВХОДНЫХ ДАННЫХ
#----------------------------------------------------------------------------

def main(plaintext,DEBUG):
    """Выполняет программу шифрования сообщения
    двухрядным зигзагообразным шрифтом"""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    cipher_text = encrypt(rails)

    if DEBUG:
        print(f"Изначальный текст: {plaintext}")
        print(f"Зашифрованный текст: {cipher_text}")

    else:
        return cipher_text


def prep_plaintext(plaintext):
    """Удаляет пробелы, заменяя их символами-заглушками"""
    stubs = ['!', '?', '.', ',', '*', ';', ':']
    message = ""

    for sym in plaintext:
        if sym != " ":
            message += sym.upper()
        else:
            message += random.choice(stubs)

    return message


def build_rails(message):
    """Строит символьную цепочку, беря каждый третий символ в сообщении"""
    first = message[::3]
    second = message[1::3]
    third = message[2::3]

    rails = first + second + third
    return rails


def encrypt(rails):
    """Разбивает шифротекст на куски по 6 букв и
    собирает в одну строку"""
    cipher_text = " ".join([rails[i:i+6] for i in range(0,len(rails),6)])

    return cipher_text



if __name__ == '__main__':
    main(plaintext)
