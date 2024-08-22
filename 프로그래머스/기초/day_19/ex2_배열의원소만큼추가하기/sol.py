# my solution
def solution(arr):
    answer = []
    for x in arr:
        for _ in range(x):
            answer.append(x)
    return answer

# best solution
def solution(arr):
    answer = []
    for x in arr:
        answer += [x]*x
    return answer



