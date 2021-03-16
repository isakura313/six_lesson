filename = 'data.txt'
try:
    with open(filename) as file:
        content = file.read()
except FileNotFoundError:
    print(f"Файл {filename} не был найден")