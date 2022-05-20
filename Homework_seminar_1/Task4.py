PointX1 = float(input('Введите координаты первой точки по оси Х: '))
PointY1 = float(input('Введите координаты первой точки по оси Y: '))
PointX2 = float(input('Введите координаты второй точки по оси Х: '))
PointY2 = float(input('Введите координаты второй точки по оси Y: '))

dinstanse = round((((PointX2 - PointX1) ** 2) +
                  ((PointY2 - PointY1) ** 2)) ** (0.5), 2)
print(dinstanse)
