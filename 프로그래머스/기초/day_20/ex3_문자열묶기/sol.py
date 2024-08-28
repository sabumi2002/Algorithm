# my solution
def solution(strArr):
    answer = 0
    strArr = [len(x) for x in strArr]
    for x in set(strArr):
        count = strArr.count(x)
        if(answer < count):
            answer = count
    return answer

# best solution (1)
def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)

# best solution (2)
def solution(strArr):
    d = {}

    for i in strArr:
        d[len(i)] = d.get(len(i), 0) + 1

    return max(d.values())
