def solution(my_string, queries):
    my_string = list(my_string)
    for i in queries:
        save = my_string[i[0] : i[1] + 1]
        save.reverse()
        my_string[i[0] : i[1] + 1] = save
    return ''.join(my_string)