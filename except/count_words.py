# -*- coding: windows-1251 -*-
def count_words(f_data):
    """ Считает и возвращает количество cлов в файле"""
    try:
        with open(f_data, encoding='windows-1251') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        return f"В этом файле под названием {f_data} {num_words} слов"

filenames = ['Bremya_strastey_chelovecheskih.txt', 'Толстой_Лев_Война_и_мир_Книга_1_royallib_ru.txt', 'data.txt']
for filename in filenames:
    print(count_words(filename))