# my solution
def solution(myString, pat):
    answer = len([idx for idx in range(len(myString)-len(pat)+1) if myString[idx:idx+len(pat)].count(pat)])
    return answer

# best solution
def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer

# tip
# [].startswith()
