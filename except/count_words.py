# -*- coding: windows-1251 -*-
def count_words(f_data):
    """ ������� � ���������� ���������� c��� � �����"""
    try:
        with open(f_data, encoding='windows-1251') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        return f"� ���� ����� ��� ��������� {f_data} {num_words} ����"

filenames = ['Bremya_strastey_chelovecheskih.txt', '�������_���_�����_�_���_�����_1_royallib_ru.txt', 'data.txt']
for filename in filenames:
    print(count_words(filename))