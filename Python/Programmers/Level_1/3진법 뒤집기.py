def solution(n):
    The_rest = 0
    Total = ''
    while n > 0:
        n, The_rest = divmod(n, 3)
        Total += str(The_rest)
    Total = Total[:len(Total)]
    return int(Total, 3)