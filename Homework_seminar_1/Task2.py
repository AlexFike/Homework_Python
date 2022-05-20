from re import X


PointX = int(input('Введите точку X: '))
PointY = int(input('Введите точку Y: '))

if  PointX > 0 and PointY > 0:
    print('1')
elif PointX < 0 and PointY > 0:
    print('2')
elif PointX < 0 and PointY < 0:
    print('3')
elif PointX > 0 and PointY < 0:
    print('4')
elif PointX == 0 and PointY != 0:
    print('X')
elif PointX != 0 and PointY == 0:
    print('Y')
else:
    print('0')