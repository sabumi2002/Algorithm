# my solution
def solution(str1, str2):
    answer = 0
    if str1 in str2:
        answer = 1
    return answer

# best solution
def solution(str1, str2):
    return int(str1 in str2)

