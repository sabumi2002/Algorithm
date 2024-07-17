# my solution
def solution(n):
    answer = 0
    if n % 2 == 1: 
        while n>0:
            answer += n
            n = n - 2 
    else:
        while n>0:
            answer += n*n
            n = n - 2
    return answer

# best solution
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])