# my solution
def solution(a, b):
    answer = int(str(b)+str(a)) if int(str(a)+str(b)) < int(str(b)+str(a)) else int(str(a)+str(b))
    return answer


# best solution
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))