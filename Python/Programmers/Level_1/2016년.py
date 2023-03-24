def solution(a, b):
    answer = ''
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Plus_day = 0

    for i in range(0, a, 1):
        Plus_day += day[i]

    Plus_day -= (day[a-1] - (b - 1))
    answer = week[Plus_day % 7]

    return answer