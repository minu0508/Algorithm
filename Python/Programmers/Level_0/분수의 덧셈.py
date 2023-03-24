import fractions

def solution(numer1, denom1, numer2, denom2):
    answer = []
    Save = 0
    
    num1 = fractions.Fraction(numer1, denom1)
    num2 = fractions.Fraction(numer2, denom2)
    Save = num1 + num2

    answer.append(Save.numerator)
    answer.append(Save.denominator)

    return answer