from asyncore import write
import random
import string

# k = int(input('degree: '))
k = 7
rand = random.randint

size = rand(1,9)
li = [(f'{rand(2,10)}x^{rand(2,k)} + ') for i in range(size)]
for i in range(size):
    if i == rand(1, size):
        li[i] = (f'{rand(1,10)} + ')
li[-1] = (f'{rand(2,9)}x^{k} = 0')
    

li = "".join(map(str, li))  

print(li)


with open('Homework_seminar_5/file.txt', 'w') as file:
    file.write(li)



