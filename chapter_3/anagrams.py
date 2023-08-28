import load_dictionary

word_list = load_dictionary.load("D:/Python's_projects/STUFF/2of4brif.txt")
anagram_list = []

name = 'Foster'
#name = str(input("Введите английское слово для поиска анаграмм: "))

print(f"Входное слово - {name}.\n")
name = name.lower()
name_sorted = sorted(name)

for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

if len(anagram_list) == 0:
    print("Анаграммы не обнаружены.")
else:
    print("Анаграммы: ", *anagram_list, sep = '\n')
