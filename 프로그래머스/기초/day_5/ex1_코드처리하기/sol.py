# my solution
def solution(code):
    answer = ""
    mode = 0
    for idx, x in enumerate(code):
        if (x == '1'): 
            mode = not(mode)
        elif ((mode == 0) and (idx % 2 == 0)):
            answer += x
        elif ((mode == 1) and (idx % 2 == 1)):
            answer += x
    if(answer == ""): answer = "EMPTY"
    return answer

# best solution
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"