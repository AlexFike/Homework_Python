string = input("Введите числа через пробел: ").split()

def convert_int_list(string):
    list = [int(string[i]) for i in range(len(string))]
    return list
# print(list)
def min_max(list):
    max = list[0]
    min = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        elif list[i] < min:
            min = list[i]
    return min, max

print(min_max(convert_int_list(string)))

# def max_and_min(arg):
#     min = int(arg[0])
#     max = int(arg[0])
#     for i in range(len(arg)):
#         if int(arg[i]) > max:
#             max = int(arg[i])
#         elif int(arg[i]) < min:
#             min = int(arg[i])
#     return max, min
# print(max_and_min(string))