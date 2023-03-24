def solution(X,Y):
    X = list(X)
    Y = list(Y)
    X_arr, Y_arr, Save_list = [], [], []
    String_number = ''

    for i in range(0, 11, 1):
        X_arr.append(X.count(str(i)))
        Y_arr.append(Y.count(str(i)))

    for j in range(len(X_arr)):
        if (X_arr[j] >= Y_arr[j]):
            String_number += str(j) * Y_arr[j]
        else:
            String_number += str(j) * X_arr[j]
    Save_list = list(String_number)
    Save_list.sort(reverse=True)

    if (len(Save_list) == 0):
        return "-1"
    elif (sum(map(int, Save_list)) == 0):
        return "0"
    else:
        answer = ''.join(Save_list)

    return answer