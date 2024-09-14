# my solution
def solution(a, b):
    answer = 0
    if (a % 2 == 1 and b % 2 == 1):
        answer = a*a + b*b
    elif (a % 2 == 1 or b % 2 == 1):
        answer = 2*(a+b)
    else:
        answer = a - b
        if answer<0:
            answer *=-1
    return answer

# best solution
def solution(a, b):
    if a % 2 and b % 2:
        return a ** 2 + b ** 2
    elif not a % 2 and not b % 2:
        return abs(a - b)
    else:
        return 2 * (a + b)
