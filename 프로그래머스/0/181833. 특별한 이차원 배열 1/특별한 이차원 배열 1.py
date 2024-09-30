def solution(n):
    answer = [[1 if i == idx else 0 for idx in range(n) ] for i in range(n)]
    return answer