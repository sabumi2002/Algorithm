# my solution
def solution(picture, k):
    answer = []
    for x in picture:
        x = ''.join([x*k for x in x])
        for j in range(k):
            answer.append(x)
    return answer

# best solution
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer

