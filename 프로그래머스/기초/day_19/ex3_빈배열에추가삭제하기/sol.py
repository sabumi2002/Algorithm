# my solution
def solution(arr, flag):
    answer = []
    for idx, b in enumerate(flag):
        if b == True:
            answer += [arr[idx]] * arr[idx] * 2
        else:
            for _ in range(arr[idx]):
                answer.pop()
    return answer


# best solution



