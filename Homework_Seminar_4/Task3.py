string = input("Введите числа через пробел: ").split()

def convert_int_list(string):
    list = [int(string[i]) for i in range(len(string))]
    return list

def min_max(list):
    min_num = min(list)
    max_num = max(list)
    return min_num, max_num

print(min_max(convert_int_list(string)))
