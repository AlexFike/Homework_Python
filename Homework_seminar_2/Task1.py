number = float(input('Введите число: '))

string_number = str(abs(number))

sum_number = 0

for i in range(len(string_number)):
    if string_number[i] != '.':
        sum_number += int(string_number[i])

print(f'Сумма всех цифр числа {number} равна: {sum_number}')
