day_weeks = int(input('Введите день недели: '))

if day_weeks > 0 and day_weeks < 6:
    print('Этот день не является выходным!')
elif day_weeks == 6 or day_weeks == 7:
    print('Это выходной день!')
else:
    print('Такого дня недели нет!')