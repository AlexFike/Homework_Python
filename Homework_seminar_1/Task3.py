quarter = int(input('Введите номер четверти: '))

if quarter == 1:
    print('X > 0 and Y > 0')
elif quarter == 2:
    print('X < 0 and Y > 0')
elif quarter == 3:
    print('X < 0 and Y < 0')
elif quarter == 4:
    print('X > 0 and Y < 0')
else:
    print('no true quarter value')