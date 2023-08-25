"""Отыскивает все палинграммы словарных пар
в файле словаря"""
import load_dictionary

word_list = load_dictionary.load("D:/Python's_projects/STUFF/2of4brif.txt")

def find_palingrams():
    """Возвращает палинграммы из словаря"""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word,rev_word[end-i:]))
                if word[:i] == rev_word[:end-i] and rev_word[:end-i] in words:
                        pali_list.append((rev_word[:end-i], word))
    return pali_list

print(f"Начало работы. Длинна словаря = {len(word_list)} слов.")

palingrams = find_palingrams()

#Отсортировать палинграммы по первому слову
palingrams_sorted = sorted(palingrams)

#Показать список палинграмм
print(f"Обнаружено {len(palingrams_sorted)} палинграмм.")
for last, next in palingrams_sorted:
    print(f"{last} {next}")
