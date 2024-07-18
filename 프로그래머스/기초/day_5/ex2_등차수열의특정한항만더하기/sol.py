# my solution
def solution(a, d, included):
    answer = sum([a + d * idx for idx, x in enumerate(included) if x])
    return answer

# best solution
def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)
