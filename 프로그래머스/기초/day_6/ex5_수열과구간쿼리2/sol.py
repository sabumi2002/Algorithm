# my solution
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        result = [x for x in arr[s:e+1] if k<x]
        result = -1 if not(result) else min(result)
        answer.append(result)
    return answer


# best solution (1)
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer
