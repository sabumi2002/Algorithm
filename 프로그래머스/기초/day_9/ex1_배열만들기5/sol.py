# my solution
def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        result = int(intStr[s:int(s)+int(l)])
        if result > k:
            answer.append(result)
    return answer

# best solution (1)
def solution(intStrs, k, s, l):
    return [int(intstr[s:s+l]) for intstr in intStrs if int(intstr[s:s+l]) > k]

# best solution (2)
def solution(intStrs, k, s, l):
    answer = []
    for x in intStrs:
        if int(x[s:s+l])>k:answer.append(int(x[s:s+l]))
    return answer
