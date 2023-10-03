"""Шифровка текста зигзагообразным шрифтом времён гражданской
войны США. Данный шифр является "двухрядным" и предназначен
для коротких сообщений.
При шифровке пробелы будут утеряны."""

#----------------------------------------------------------------------------
#ВХОДНЫЕ ДАННЫЕ:
plaintext = """Давай пересечём реку и отдохнём в тени деревьев"""
DEBUG = True
#КОНЕЦ ВХОДНЫХ ДАННЫХ
#----------------------------------------------------------------------------

def main():
    """Выполняет программу шифрования сообщения
    двухрядным зигзагообразным шрифтом"""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    cipher_text = encrypt(rails)

    if DEBUG:
        print(f"Изначальный текст: {plaintext}")
        print(f"Зашифрованный текст: {cipher_text}")


def prep_plaintext(plaintext):
    """Удаляет пробелы и переводит текст в верхний регистр"""
    message = "".join(plaintext.split())
    message = message.upper()
    return message


def build_rails(message):
    """Строит символьныую цепочку, беря каждый
    второй символ в сообщении"""
    evens = message[::2]
    odds = message[1::2]

    rails = evens + odds
    return rails


def encrypt(rails):
    """Разбивает шифротекст на куски по 5 букв и
    собирает в одну строку"""
    cipher_text = ' '.join([rails[i:i+5] for i in range(0, len(rails),5)])

    return cipher_text



if __name__ == '__main__':
    main()
