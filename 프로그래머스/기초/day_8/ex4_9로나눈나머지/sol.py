# my solution
def solution(number):
    answer = sum([int(x) for x in number])%9
    return answer

# best solution
def solution(number):
    return sum(map(int, number)) % 9
