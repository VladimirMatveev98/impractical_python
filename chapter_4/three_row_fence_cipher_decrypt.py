"""Дешифровка текста трёхрядным зигзагообразным шрифтом
времён гражданской войны США.
При расшифровке восстанавливаются пробелы."""

import math
import itertools

#------------------------------------------------------------------------------
#ВХОДНЫЕ ДАННЫЕ:
cipher_text = """ДАПЕЧ, КИТХМ, НДЕЕАЙ ЕСЁРУ. ДН:ТИЕ ВВВ,РЕ МЕ*ООЁ ВЕ.РЬ"""
DEBUG = True
#КОНЕЦ ВХОДНЫХ ДАННЫХ
#------------------------------------------------------------------------------

def main(cipher_text,DEBUG):
    """Выполняет программу для дешифровки двухрядного
    зигзагообразного шрифта."""
    message = prep_ciphertext(cipher_text)
    row1, row2, row3 = split_rails(message)
    message = decrypt(row1, row2, row3)

    if DEBUG:
        print(f"\nИсходный шифр: {cipher_text}.\n")
        print(f"Ряд 1: {row1}. \nРяд 2: {row2}.\nРяд 3: {row3}.\n")
        print(f"Расшифрованное сообщение: {message}.")
    else:
        return message


def prep_ciphertext(cipher_text):
    """Удаляет пробелы из исходного сообщения и заменяет
    символы-заглушки на пробелы"""
    message = "".join(cipher_text.split())
    stubs = ['!', '?', '.', ',', '*', ';', ':']

    for sym in stubs:
        message = message.replace(sym, ' ')

    return message


def split_rails(message):
    """Разбивает исходное сообщение на три части,
    округляя первые две в большую сторону"""
    start = math.ceil(len(message)/3)
    stop = start * 2
    row1 = message[:start]
    row2 = message[start:stop]
    row3 = message[stop:]

    return row1, row2, row3


def decrypt(row1, row2, row3):
    """Строит список, чередуя символы из трёх цепочек,
    и возвращает текст, собранный из этого списка"""
    plaintext = []
    for i in range(len(row1)):
        plaintext.append(row1[i])
        plaintext.append(row2[i])
        try:
            plaintext.append(row3[i])
        except IndexError:
            pass

    plaintext = "".join(plaintext)

    return plaintext



if __name__ == '__main__':
    main(cipher_text, DEBUG)
