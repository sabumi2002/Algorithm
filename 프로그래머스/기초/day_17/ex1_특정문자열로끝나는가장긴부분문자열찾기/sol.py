# my solution
def solution(myString, pat):
    answer = myString[:myString.rindex(pat)+len(pat)]
    return answer

# best solurion
def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]


