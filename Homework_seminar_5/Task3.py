
n = [1, 2, 3, 5, 1, 5, 3, 10]

print(n)
unique =  [n[i] for i in range(len(n)) if n[i] not in n[i+1::] and n[i] not in n[:i-1:]] 

# for i in range(len(n)):
#     if n[i] not in n[i+1::] and n[i] not in n[:i-1:]:
#         unique.append(n[i])

print(unique)
