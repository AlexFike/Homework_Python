number = int(input('Введите число N: '))

list_number = []
save_number = 1

for i in range(1, number+1):
    save_number *=(number - (number - i))
    list_number.append(save_number)
print(list_number)