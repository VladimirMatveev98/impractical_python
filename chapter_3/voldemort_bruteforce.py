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
    filter_2 = trigrams_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)


def prep_words(name, word_list_ini):
    print(f"Длина первоначального списка: {len(word_list_ini)}")
    len_name = len(name)
    word_list = [w.lower() for w in word_list_ini if len(word) == len_name]
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
