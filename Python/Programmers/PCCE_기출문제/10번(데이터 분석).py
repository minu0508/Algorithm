def solution(data, ext, val_ext, sort_by):
    answer = []

    if sort_by == "code":
        data.sort(key = lambda x : x[0])
    elif sort_by == "date":
        data.sort(key = lambda x : x[1])
    elif sort_by == "maximum":
        data.sort(key = lambda x : x[2])
    elif sort_by == "remain":
        data.sort(key = lambda x : x[3])

    if ext == "code":
        for i in range(len(data)):
            if (val_ext > data[i][0]):
                save_list = data[i]
                answer.append(save_list)
    elif ext == "date":
        for i in range(len(data)):
            if (val_ext > data[i][1]):
                save_list = data[i]
                answer.append(save_list)
    elif ext == "maximum":
        for i in range(len(data)):
            if (val_ext > data[i][2]):
                save_list = data[i]
                answer.append(save_list)
    elif ext == "remain":
        for i in range(len(data)):
            if (val_ext > data[i][3]):
                save_list = data[i]
                answer.append(save_list)

    return answer