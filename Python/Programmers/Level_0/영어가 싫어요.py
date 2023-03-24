def solution(numbers):
    answer = 0
    a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    Result_str = ''

    for i in range(10):
        num = numbers.count(a[i])
        if (num >= 1):
            Result_str += str(a.index(a[i]))
    answer = int(Result_str)
    return answer