import posixpath 

def read_file_list(link):
    file = open(link, 'r')
    read_file = file.read() + ''
    list_numbers = list(map(int, read_file.split()))
    file.close()
    return list_numbers

def check(A):
    for i in range(A[0],len(A)+1):
        if A[i] - 1 != A[i -1]:
            result = i + 1
            break
    return result

print(check(read_file_list('Homework_seminar_5/file2.txt')))
