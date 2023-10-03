"""Дешифровка текста зигзагообразным шрифтом времён гражданской
войны США. Данный шифр является "двухрядным" и предназначен
для коротких сообщений.
При расшифровке не восстанавливаются пробелы."""

import math
import itertools

#----------------------------------------------------------------------------
#ВХОДНЫЕ ДАННЫЕ:
cipher_text = """ДВЙЕЕ ЕЁРКИ ТОНМТ НДРВЕ ААПРС ЧМЕУО ДХЁВЕ ИЕЕЬВ"""
DEBUG = True
#КОНЕЦ ВХОДНЫХ ДАННЫХ
#----------------------------------------------------------------------------

def main():
    """Выполняет программу для дешифровки двухрядного
    зигзагообразного шрифта."""
    message = prep_ciphertext(cipher_text)
    row1,row2 = split_rails(message)
    message = decrypt(row1,row2)

    if DEBUG:
        print(f"\nИсходный шифр: {cipher_text}.\n")
        print(f"Ряд 1: {row1}. \nРяд 2: {row2}.\n")
        print(f"Расшифрованное сообщение: {message}.")


def prep_ciphertext(cipher_text):
    """Удаляет пробелы"""
    message = "".join(cipher_text.split())
    return message


def split_rails(message):
    """Разбивает сообщение на два, округляя
    в большую сторону первый ряд"""
    row1_len = math.ceil(len(message)/2)
    row1 = message[:row1_len]
    row2 = message[row1_len:]
    return row1, row2


def decrypt(row1, row2):
    """Строит список, чередуя символы из
    двух цепочек, и возвращает его"""
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1.lower())
        plaintext.append(r2.lower())

    #itertools.zip_longest в конце работы возвращает None.
    #Актуально для сообщений нечётной длинны.
    if None in plaintext:
        plaintext.pop()

    #Собираем список символов в текстовую строку.
    plaintext = "".join(plaintext)

    return plaintext



if __name__ == '__main__':
    main()
