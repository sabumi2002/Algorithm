# my solution
def solution(n, k):
    answer = [x for x in range(1, n+1) if x % k == 0]
    return answer


# best solution
def solution(n, k):
    return [i for i in range(k,n+1,k)]


