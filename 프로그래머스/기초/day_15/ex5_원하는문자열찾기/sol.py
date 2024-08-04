# my solution
def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    answer = 1 if myString.find(pat) >= 0 else 0
    return answer

# best solution
def solution(myString, pat):
    return int(pat.lower() in myString.lower())

