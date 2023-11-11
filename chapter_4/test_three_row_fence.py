"""Автоматический юнит-тест для трёхрядного шифра.
Должен включать варианты с разной длинной текста, а именно:
С длинной текста, кратной 3;
Длинна текста, делённая на 3, даёт остаток 1;
Длинна текста, делённая на 3, даёт остаток 2.
Проверять как шифровку, так и расшифровку.
Описать все проверки в разделе документации.
Всего 6 или 8 тестов.
"""

import unittest
import three_row_fence_cipher_encrypt as encrypt
import three_row_fence_cipher_decrypt as decrypt

test_case_1 = ("""Давай пересечём реку и отдохнём в тени деревьев""",
               """ДАПЕЧ, КИТХМ, НДЕЕАЙ ЕСЁРУ. ДН:ТИЕ ВВВ,РЕ МЕ*ООЁ ВЕ.РЬ""")

test_case_2 = ("""*""",
               """*""")

test_case_3 = ("""*""",
               """*""")


class Test_encrypt_decrypt(unittest.TestCase):
    #-------------------Тесты шиврования-----------------------------
    def test_len_message_47_encrypt(self):
        """Тестирует шифровку сообщения длиной 47 символов"""
        #Заглушки, используемые для пробелов
        stubs = ['!', '?', '.', ',', '*', ';', ':']

        #Распаковка данных для проверки
        test_res_1_1 = encrypt.main(test_case_1[0],False)
        correct_res = test_case_1[1]

        for sym in stubs:
            #Заменяем "пробелы" на единый символ
            test_res_1_1 = test_res_1_1.replace(sym, '*')
            correct_res = correct_res.replace(sym, '*')

        self.assertEqual(test_res_1_1, correct_res)


    def test_len_message_47_decrypt(self):
        """Тестирует расшифровку сообщения длиной 47 символов"""
        test_res = decrypt.main(test_case_1[1],False)
        correct_res = test_case_1[0].upper()
        self.assertEqual(test_res, correct_res)

    #-----------Тесты отдельных функций------------------------

    def test_prepare_encrypt(self):
        """Тестирует функцию подготовки текста к шифровке"""
        stubs = ['!', '?', '.', ',', '*', ';', ':']
        test_res = encrypt.prep_plaintext(test_case_1[0])

        for sym in stubs:
            #Заменяем "пробелы" на единый символ
            test_res = test_res.replace(sym, '*')

        correct_res = "Давай*пересечём*реку*и*отдохнём*в*тени*деревьев"
        correct_res = correct_res.upper()

        self.assertEqual(test_res, correct_res)


    def test_build_rails(self):
        """Тестирует построение трёх рядов 'цепочки' """
        pass


    def test_encrypt(self):
        """Тест непостредственно 'сборки' шифротекста по
        символам 'цепочки', полученной из прошлой функции."""
        pass



if __name__ == "__main__":
  unittest.main()
