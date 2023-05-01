import string

alp_low = string.ascii_lowercase
alp_up = string.ascii_uppercase
str = input()
answer = ''

for i in str:
    if (alp_low.count(i) >= 1):
        answer += i.upper()
    else:
        answer += i.lower()

print(answer)    