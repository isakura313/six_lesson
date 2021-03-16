data = input("Введите полезную информацию")
for i in range(0, 10):
    with open(f'new/{i}.txt', 'a') as f:
        f.write(data + "\n")
