chiper_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

DEBUG = False
COLS = 4
ROWS = 5
KEY = '-1 2 -3 4'

cipher_list = list(chiper_text.split())

translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

key_int = [int(i) for i in KEY.split()]

for k in key_int:
    if k < 0:
        col_items = cipher_list[start:stop]
    elif k > 0:
        col_items = list((reversed(cipher_list[start:stop])))

    translation_matrix[abs(k)-1] = col_items
    start += ROWS
    stop += ROWS

    if DEBUG:
        print("Новая итерация цикла!")
        print(f"Шифр = {chiper_text}")
        print(f"Переводная матрица = {translation_matrix}")
        print(f"Длина ключа = {len(key_int)}\n")

for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + " "

print(f"Расшифрованный текст = {plaintext}")
