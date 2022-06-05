f = int(input('Введите число: '))


def fibo(n):
    list_fibo = []
    fib1, fib2 = 1, 1
    for i in range(n):
        list_fibo.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2
    fib1, fib2 = 0, 1
    for i in range(n+1):
        list_fibo.insert(0, fib1)
        fib1, fib2 = fib2, fib1 - fib2
    return list_fibo

print(fibo(f))

