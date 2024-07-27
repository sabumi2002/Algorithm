# my solution
def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        for x in arr[a:b+1]:
            answer.append(x)
    return answer


# best solution (1)
def solution(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1:e1+1] + arr[s2:e2+1]

# best solution (2)
def solution(arr, intervals):
    answer = []
    for a,b in intervals: answer+=arr[a:b+1]
    return answer

