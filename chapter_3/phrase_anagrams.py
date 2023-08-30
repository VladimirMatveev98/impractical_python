import sys
from collections import Counter
import load_dictionary

#Получить список слов
dict_file = load_dictionary.load("D:/Python's_projects/STUFF/2of4brif.txt")
#Удалить однобуквенные "слова"
dict_file = load_dictionary.optimize(dict_file)

#Добавить необходимые предлоги 'a' и 'i'
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

ini_name = input("Введите имя: ")

def find_anagrams(name, word_list):
    """Прочитать имя и список слов и
    показать все анаграммы в имени"""
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
            if Counter(test) == word_letter_map:
                anagrams.append(word)

    print(*anagrams, sep='\n')
    print()
    print(f"Оставшиеся буквы = {name}")
    print(f"Число оставшихся букв = {len(name)}")
    print(f"Число остальных анаграмм = {len(anagrams)}")


def process_choice(name):
    """Позволяет пользователю выбрать часть анаграммы
    из списка и добавляет эту часть к итоговому результату.
    Возвращает выбранную часть и оставшиеся буквы.
    """

    while True:
        msg = """\nВведите анаграмму из списка ИЛИ нажмите ENTER,
чтобы начать сначала, либо введите # для выхода. >> """

        choice = input(msg)
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
            left_over_list = list(name)
            for letter in candidate:
                if letter in left_over_list:
                    left_over_list.remove(letter)
            if len(name) - len(left_over_list) == len(candidate):
                break
            else:
                print("Не сработает, пробуем ещё один вариант.")

    name = ''.join(left_over_list)
    return choice, name


def main():
    """Управляет остальными функциями. В бесконечном цикле собирает
    анаграмму по частям с участием пользователя."""
    name = ''.join(ini_name.lower().split())
    name = name.replace('-', '')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f"Длина анаграммного словосочетания = {len(temp_phrase)}")

            find_anagrams(name, dict_file)
            print("Текущее анаграммное словосочетание - ", end = '')
            print(phrase)

            choice, name = process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print('\n***** ГОТОВО! *****\n')
            print(f'Полученная анаграмма = {phrase}.')
            msg = '\n\nПробуем ещё раз -> ENTER, выход -> n. >>'
            try_again = input(msg)
            if try_again.lower() == 'n':
                running = False
                sys.exit()
            else:
                main()



if __name__ == '__main__':
    main()
