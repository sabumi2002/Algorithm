# my solution
import math
def solution(my_string, m, c):
    strArr = [my_string[m*x:m*x+m] for x in range(math.ceil(len(my_string)/m))]
    answer = ''.join([strArr[x][c-1] for x in range(len(strArr))])
    return answer

# best solution
def solution(my_string, m, c):
    return ''.join([ my_string[i * m + c-1] for i in range(len(my_string) // m)])

