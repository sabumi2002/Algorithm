# my solution
def solution(myStr):
    answer = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    answer = answer.split(' ')
    answer = [x for x in answer if x != '']
    answer = ["EMPTY"] if len(answer) == 0 else answer
    return answer


# best solution
import re
def solution(myStr):
    answer = [m for m in re.split('a|b|c',myStr) if m]
    if len(answer)==0:
        answer=["EMPTY"]

    return answer


