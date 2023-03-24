num = int(input())
num_line = 0
max_num = 0

while True:
    if num > max_num:
        num_line += 1
        max_num += num_line
    else:
        break

A = max_num - num
mom = 0
son = 0
if num_line%2 == 0:
    son = num_line - A
    mom = A + 1
else:
    son = A + 1
    mom = num_line - A
    
print("%d/%d" %(son, mom))