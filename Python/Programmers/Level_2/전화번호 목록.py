# def solution(phone_book):
#     answer = True

#     for i in phone_book:
#         for j in range(0, len(phone_book), 1):
#             if (i == phone_book[j]):
#                 pass
#             else:
#                 if (len(i) < len(phone_book[j])):
#                     if (phone_book[j][:len(i)] == i):
#                         answer = False
#                         break

#                 else:
#                     if (i[:len(phone_book[j])] == phone_book[j]):
#                         answer = False
#                         break
#     return answer

# Hash를 이용한 것이 아니며, 효율성 0점

def solution(phone_book):
    answer = True
    hash = {}

    for i in phone_book:
        hash[i] = 1

    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            if temp in hash and temp != i:
                answer = False
    
    return answer