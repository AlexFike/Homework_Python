n = input('Введите два числа: ').split()

def scm(first_namber, second_number):
    count = min(first_namber, second_number)
    while True:
        if count%first_namber==0 and count%second_number==0:
            break
        count += 1
    return count
print(scm(int(n[0]), int(n[1])))