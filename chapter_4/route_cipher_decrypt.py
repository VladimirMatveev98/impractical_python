"""
Расшировывает путь маршрутного шифра.

Предназначено для полнословных перестановочных шифров с
переменными строками и столбцами. Исходит из допущения,
что шифрование началось вверху или внизу столбца.
Ключ указывает на порядок чтения столбцов и направление прохождения.
Отрицательные числа означают чтение снизу вверх.
Положительные - сверху вниз.

Необходимые входные данные - текстовое сообщение, число столбцов,
число строк, символьная цепочка с ключом.

Печатает расшифрованный текст.
"""

import sys

#==================================================================
#Входные данные:

#дешифруемая цепочка:
cipher_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

#Число столбцов в перестановочной матрице:
COLS = 4

#Число строк в перестановочной матрице:
ROWS = 5

#Ключ с пробелами между числами:
KEY = "-1 2 -3 4"

#КОНЕЦ ВХОДНЫХ ДАННЫХ.
#==================================================================

def main():
    """Выполняет программу и печатает расшифрованный текст"""
    print(f"Шифротекст = {cipher_text}")
    print(f"Проверка {COLS} столбцов.")
    print(f"Проверка {ROWS} строк.")
    print(f"Проверяемый ключ - {KEY}")

    cipher_list = list(cipher_text.split())
    validate_col_row(cipher_list)
    key_int = key_to_int(KEY)
    translation_matrix = build_matrix(key_int, cipher_list)
    plaintext = decrypt(translation_matrix)

    print(f"Открытый текст: {plaintext}")


def validate_col_row(cipher_list):
    """Проверяет соответствие длинны сообщения
    и входных столбцов со строками"""
    factors = []
    len_cipher = len(cipher_list)
    for i in range(2, len_cipher):
        if len_cipher % i == 0:
            factors.append(i)

    print(f"Длина шифра = {len_cipher}")
    print(f"Примелемые значения столбцов/строк: {factors}")

    if ROWS * COLS != len_cipher:
        print("Входные строки и столбцы не являются",
              "корректными для длины шифра. Завершение работы.")
        sys.exit(1)


def key_to_int(KEY):
    """Превращает ключ в список целых чисел и проверяет
    его на допустимость"""
    key_int = [int(i) for i in KEY.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
        or 0 in key_int:
        print("Ошибка ключа. Завершение работы.")
        sys.exit(1)
    else:
        return key_int


def build_matrix(key_int, cipher_list):
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0:
            col_items = cipher_list[start:stop]
        elif k > 0:
            col_items = list(reversed(cipher_list[start:stop]))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS

    return translation_matrix


def decrypt(translation_matrix):
    plaintext = ""
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + " "

    return plaintext



if __name__ == '__main__':
    main()
