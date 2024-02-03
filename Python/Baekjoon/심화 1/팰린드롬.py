a = list(input())
first = [i for i in a]
a.reverse()
second = [i for i in a]

if (''.join(first) == ''.join(second)):
    print(1)
else:
    print(0)