a = ['1', 'ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
b = input()
total = 0

for i in a:
    for j in i:
        for k in b:
            if j == k:
                total += a.index(i) + 2

print(total)