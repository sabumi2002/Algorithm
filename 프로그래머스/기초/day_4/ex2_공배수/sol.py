# my solution
def solution(number, n, m):
    answer = 1 if int(not(number % n))+int(not(number % m))>1 else 0
    return answer

# best solution
def solution(number, n, m):
    return int(number%n == 0 and number%m == 0)