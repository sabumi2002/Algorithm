# my solution
def solution(strArr):
    answer = [x.lower() if idx % 2 == 0 else x.upper() for idx, x in enumerate(strArr)]
    return answer

# best solution



