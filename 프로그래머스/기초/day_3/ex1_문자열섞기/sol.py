# my solution
def solution(str1, str2):
    answer = ''
    for index in range(len(str1)):
        answer += str1[index] + str2[index]
    return answer

# best solution
def solution(str1, str2):
    answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    return answer