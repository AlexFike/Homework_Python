PointX = int(input('Введите координаты точки на оси X: '))
PointY = int(input('Введите координаты точки на оси Y: '))

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