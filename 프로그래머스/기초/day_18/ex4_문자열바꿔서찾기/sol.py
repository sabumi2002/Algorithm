# my solution
def solution(myString, pat):
    answer = ''
    for x in myString:
        if x == 'A':
            answer += 'B'
        elif x == 'B':
            answer += 'A'
    answer = 1 if answer.find(pat) >= 0 else 0
    return answer


# best solution
def solution(myString, pat):
    return int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString)

