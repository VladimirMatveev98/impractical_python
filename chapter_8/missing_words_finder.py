import sys
import pprint
from string import punctuation
import json
from nltk.corpus import cmudict

#Словарь произношения
cmudict = cmudict.dict()


def load_haiku(filename):
    """Открывает и возвращает  тренировочный корпус в виде множества."""
    with open(filename) as f:
        haiku = set(f.read().replace('-', ' ').split())
        return haiku


def cmudict_missing(word_set):
    """Ищет и возвращает слова в множетстве word_set, которые
    отсутствуют в cmudict."""
    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("`s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)

    print("Исключения:")
    print(*exceptions, sep='\n')

    print(f"Всего уникальных слов в корпусе хокку: {len(word_set)}")
    print(f"Всего слов в корпусе слов не из cmudict: {len(exceptions)}")
    membership = (1 - (len(exceptions) / len(word_set))) * 100
    membership = round(membership, 2)
    print(f"Членство в cmudict = {membership}%")
    return exceptions


def make_exceptions_dict(exceptions_set):
    """Возвращает словарь слов и количества слогов из множества слов."""
    missing_words = {}
    print("Введите число слогов в слове. Ошибки можно исправиь в конце.")
    for word in exceptions_set:
        while True:
            num_sylls = input(f'Введите число слогов в слове "{word}": ')
            if num_sylls.isdigit():
                break
            else:
                print("ОШИБКА: недопустимый ввод. Ввод должен быть цифрой!", file=sys.stderr)

        missing_words[word] = int(num_sylls)
        pprint.pprint(missing_words, width=1)

        print("Внести изменения в словарь перед сохранением?")
        print("""
        0 - Выйти и сохранить;
        1 - добавить слово либо изменить количество слогов;
        2 - Удалить слово.
        """)

        while True:
            choice = input("Ваш выбор: >> ")
            if choice == '0':
                break
            elif choice == '1':
                word = input("Добавляемое или изменяемое слово: ")
                num_sylls = input(f'Введите число слогов в слове "{word}": ')
                missing_words[word] = int(num_sylls)
            elif choice == '2':
                word = input("Введите удаляемое слово: ")
                missing_words.pop(word, None)

        print("Изменения в новых словах и слогах: ")
        pprint.pprint(missing_words, width=1)

        return missing_words


def save_exceptions(missing_words):
    """Сохраняет словарь исключений в виде json-файла."""
    json_string = json.dumps(missing_words)
    f = open('missing_words.json', 'w')
    f.write(json_string)
    f.close()
    print("Файл сохранён как missing_words.json")


def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input("\nПостроить словарь исключений вручную (y/n)?\n>> ")
    if build_dict.lower() == 'n':
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
        save_exceptions(missing_words_dict)


if __name__ == "__main__":
    main()
