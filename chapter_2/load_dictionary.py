"""Загружает текстовый файл как список слов.

Аргументы:
- Имя текстового файла (или путь к файлу)
Исключения:
- IOErrer, если имя файла не найдено.
Возвращает список всех слов в файле в нижнем регистре.
Требует - import sys"""
import sys

def load(file):
    """Открывает текстовый файл и возвращает список
    слов в нижнем регистре"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nОшибка при открытии {}. Завершение программы.".
              format(e, file))
        sys.exit(1)

if __name__ == '__main__':

    PATH = "D:/Python's_projects/STUFF/2of4brif.txt"
    print(load(PATH))
