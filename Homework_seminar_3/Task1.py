def sum_odd_numbers(value):


    sum = 0
    for i in range(len(value)):
        if i % 2 != 0:
            sum += value[i]
    return sum


list = [2, 3, 5, 9, 3, 3, 3, 3]
print(sum_odd_numbers(list))
