import sys
input = sys.stdin.readline

All = [i+1 for i in range(30)]
student = sorted([int(input()) for i in range(28)])

for i in All:
    if student.count(i) == 0:
        print(i)