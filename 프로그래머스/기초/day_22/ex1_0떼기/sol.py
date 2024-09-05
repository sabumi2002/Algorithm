# my solution
def solution(n_str):
    check = False
    answer = ""
    for x in n_str:
        if x != "0":
            check= True
        if check:
            answer += x
    return answer

# best solution(1)
def solution(n_str):
    return n_str.lstrip('0')

# best solution(2)
def solution(n_str):
    return str(int(n_str))
