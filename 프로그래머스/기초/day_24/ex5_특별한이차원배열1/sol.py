# my solution
def solution(n):
    answer = [[1 if i == idx else 0 for idx in range(n) ] for i in range(n)]
    return answer

# best solution
def solution(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer
