import sys
import string

def load_text(file):
    """Загружает текстовый файл в виде цепочки символов"""
    with open(file) as f:
        return f.read().strip()


def solve_null_cipher(message, lookahead):
    """Расшифровывает нулевой шифр, основываясь
    на числе букв после знака препинания.
    message - текст нулевого шифра без пробелов.
    lookahead - искомая буква после знака препинания."""

    for i in range(1, lookahead + 1):
        plaintext = ''
        count = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1

            if count == i:
                plaintext += char

        print(f"Используя сдвиг {i} после знака препинания = {plaintext}\n")


def main():
    """Загружает текст и отгадывает нулевой шифр"""
    #filename = input("Введите полное имя файла для расшифровки: ")
    filename = 'trevanion.txt'
    try:
        loaded_message = load_text(filename)
    except IOError as e:
        print(f"{e}. Возможно, такой файл не существует.")
        sys.exit(1)
    print("\nПервоначальное сообщение: \n", loaded_message, "\n")

    #Удалить пробелы
    message = ''.join(loaded_message.split())

    #Получить от пользователя диапазон ключей
    user_message = "Введите номер искомой буквы после знака препинания: "
    lookahead = int(input(user_message))

    #Вызов функции декодирования
    solve_null_cipher(message, lookahead)



if __name__ == '__main__':
    main()
