# my solution
def solution(arr, k):
    answer = []
    for x in arr:
        if x not in answer and len(answer) < k:
            answer += [x]
    if len(answer) < k:
        for x in range(k-len(answer)):
            answer += [-1]
    return answer

# best solution
def solution(arr, k):
    res = list(dict.fromkeys(arr))
    res.extend([-1] * max(0, k - len(res)))
    return res[:k]



