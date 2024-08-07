# my solution
def solution(myString):
    answer = []
    for x in myString:
        if x == 'a':
            answer.append(x.upper())
        elif x != 'A' and x.isupper():
            answer.append(x.lower())
        else:
            answer.append(x)
    answer = ''.join(answer)
    return answer


# best solution
def solution(myString):
    return myString.lower().replace('a', 'A')


