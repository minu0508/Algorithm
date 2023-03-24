def solution(A, B):
    answer = 0

    if (A != B):
        A = list(A)

        for _ in range(len(A)):
            A_word = ''
            answer += 1
            A.insert(0, A.pop())
            for i in A:
                A_word += i
            
            if(A_word == B):
                return answer
            
        return(-1)
    return answer