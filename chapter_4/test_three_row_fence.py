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
    def test_len_message_47_encrypt(self):
        #Заглушки, используемые для пробелов
        stubs = ['!', '?', '.', ',', '*', ';', ':']

        #Распаковка данных для проверки
        test_res_1_1 = encrypt.main(test_case_1[0],False)
        test_res_1_2 = test_case_1[1]

        for sym in stubs:
            #Заменяем "пробелы" на единый символ
            test_res_1_1 = test_res_1_1.replace(sym, ' ')
            test_res_1_2 = test_res_1_2.replace(sym, ' ')

        self.assertEqual(test_res_1_1, test_res_1_2)


if __name__ == "__main__":
  unittest.main()
