# my solution
def solution(strArr):
    answer = [x for x in strArr if x.find('ad')<0]
    return answer



# best solution
def solution(strArr):
    return [word for word in strArr if 'ad' not in word]


