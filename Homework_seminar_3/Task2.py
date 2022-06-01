def mult_element(value):
    list = []
    for i in range(len(value) // 2 + len(value) % 2):
        add_element = value[i] * value[(len(value) - i) - 1]
        list.append(add_element)
    return list

test_list = [2, 3, 4, 5, 6]
print(mult_element(test_list))
