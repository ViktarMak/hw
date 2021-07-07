m = int(input('Введите номер месяца: '))
if m < 1 or m > 12:
    raise ValueError('неверный номер месяца')
elif m <= 2 or m == 12:
    print('Зима')
elif m <= 5:
    print('Весна')
elif m <= 8:
    print('Лето')
else:
    print('Осень')