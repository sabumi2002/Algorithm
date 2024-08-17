# my solution
def solution(myString):
    answer = sorted([x for x in myString.split('x') if x not in ""])
    return answer



# best solution
def solution(myString):
    return sorted(ch for ch in myString.split('x') if ch)

