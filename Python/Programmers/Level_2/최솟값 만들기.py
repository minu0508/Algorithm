def solution(A,B):
    A = sorted(A, reverse = True)
    B.sort()
    return sum([A[i] * B[i] for i in range(0, len(A), 1)])

solution([1, 4, 2], [5, 4, 4])