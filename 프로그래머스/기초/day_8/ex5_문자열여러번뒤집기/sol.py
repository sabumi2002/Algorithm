# my solution
def solution(my_string, queries):
    answer = list(my_string)
    for s, e in queries:
        for idx in range(s, e+1):
            answer[e-idx+s] = my_string[idx]
        my_string = list(answer)
    answer = ''.join(answer)
    return answer

# best solution
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)
