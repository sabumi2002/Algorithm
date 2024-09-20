def solution(picture, k):
    answer = []
    for x in picture:
        x = ''.join([x*k for x in x])
        for j in range(k):
            answer.append(x)
    return answer