def difference_min_and_max(value):
    for i in range(len(value)):
        if i == 0:
            min = value[i]
            max = value[i]
        elif value[i] < min:
            min = value[i]
        elif value[i] > max:
            max = value[i]

    result = round(abs((max - int(max)) - (min - int(min))), 2)
    return result

test_list = [1.1, 1.2, 3.1, 5, 10.01]
print(difference_min_and_max(test_list))