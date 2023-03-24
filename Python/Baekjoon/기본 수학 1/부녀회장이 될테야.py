T = int(input())
total = []

for i in range(T):
    person = []
    k = int(input())
    n = int(input())
    for p in range(1, n+1, 1):
        person.append(p)
        
    if k == 0:
        print(n)
    else:
        for j in range(k):
            for k in range(1, n):
                person[k] += person[k-1]
        total.append(person[-1])
    
for m in range(0, len(total), 1):
    print(total[m])