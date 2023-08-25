"""Добавляет в список все палиндромы из словаря
и выводит их на печать"""

import load_dictionary
world_list = load_dictionary.load("D:/Python's_projects/STUFF/2of4brif.txt")
palindromes = []

for word in world_list:
    if len(word) > 1 and word == word [::-1]:
        palindromes.append(word)

print(f"Число обнаруженных паиндромов: {len(palindromes)}\n")
print(*palindromes, sep = '\n')
