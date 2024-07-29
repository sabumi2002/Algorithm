# my solution
def solution(numbers, n):
    answer = 0
    for x in numbers:
        answer += x
        if answer > n:
            return answer



# best solution
def solution(numbers, n):
    return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)



