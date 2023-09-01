import sys
from itertools import permutations
from collections import Counter
import load_dictionary

PATH = "D:/Python's_projects/STUFF/2of4brif.txt"
TRIGRAMS = "D:/Python's_projects/STUFF/least-likely_trigrams.txt"

def main():
    name = 'tmvoordle'
    name = name.lower()

    word_list_ini = load_dictionary.load(PATH)
    word_list_ini = load_dictionary.optimize(word_list_ini)
    trigrams_filtered = load_dictionary.load(TRIGRAMS)

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)


def prep_words(name, word_list_ini):
    print(f"Длина первоначального списка: {len(word_list_ini)}")
    len_name = len(name)
    word_list = [w.lower() for w in word_list_ini if len(w) == len_name]
    print(f"Длина нового списка: {len(word_list)}")
    return word_list


def cv_map_words(word_list):
    """Спроецировать буквы сова в гласные и согласные"""
    vowels = 'aeiouy'
    cv_mapped_words = []
    for word in word_list:
        temp = ''
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'

        cv_mapped_words.append(temp)

    total = len(set(cv_mapped_words))
    #Целевая доля устраняемых
    target = 0.05
    #Получить число элементов в целевой доле
    n = int(total * target)
    count_pruned = Counter(cv_mapped_words).most_common(total - n)
    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print(f"Длина множества filtered_cv_map: {len(filtered_cv_map)}")
    return filtered_cv_map


def cv_map_filter(name, filtered_cv_map):
    perms = {''.join(i) for i in permutations(name)}
    print(f"Длина первоначального множества: {len(perms)}")
    vowels = 'aeiouy'
    filter_1 = set()
    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'

        if temp in filtered_cv_map:
            filter_1.add(candidate)
    print(f"Вариантов после фильтра 1: {len(filter_1)}")

    return filter_1


def trigram_filter(filter_1, trigrams_filtered):
    """Удаляет маловероятные триграммы"""
    filtered = set()
    for candidate in filter_1:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate:
                filtered.add(candidate)
    filter_2 = filter_1 - filtered
    print(f"Вариантов после фильтра 2: {len(filter_2)}")

    return filter_2


def letter_pair_filter(filter_2):
    """Удаляет маловероятные буквенные пары"""
    filtered = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv',
               'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']

    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd',
                          'rl', 'rm', 'rt', 'rv', 'tl', 'tm']

    for candidate in filter_2:
        for r in rejects:
            if r in candidate:
                filtered.add(candidate)
        for fp in first_pair_rejects:
            if candidate.startswith(fp):
                filtered.add(candidate)
    filter_3 = filter_2 - filtered
    print(f"Вариантов после фильтра 3: {len(filter_3)}")
    if 'voldemort' in filter_3:
        print("Воландеморт найден!")

    return filter_3


def view_by_letter(name, filter_3):
    """Фильтрует анаграммы по первой букве"""
    print("Остальные буквы: {}".format(name))
    first = input("Выберите стартовую букву или нажмите ENTER: ")

    subset = []
    for candidate in filter_3:
        if candidate.startswith(first):
            subset.append(candidate)
    print(*sorted(subset), sep = '\n')
    print(f"Число вариантов, начинающися с {first} = {len(subset)}")

    try_again = input("""Нажмите ENTER что бы попробовать ещё раз или
    введите любой символ для выхода: """)
    if try_again.lower() == '':
        view_by_letter(name, filter_3)
    else:
        sys.exit()



if __name__ == '__main__':
    main()
