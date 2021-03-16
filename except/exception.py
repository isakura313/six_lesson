print("Вводи числа, и я разделю их")
while True:
    fn = input('Введите первое число')
    if fn == 'q':
        break
    sn = int(input('Введите второе число'))
    try:
        print(int(fn)/sn)
    except ZeroDivisionError:
        print("Не надо делить на ноль")
    else:
        print('infinity')

