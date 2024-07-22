# my solution
def solution(l, r):
    answer = []
    result = False

    for num in range(l, r+1):
        num = str(num)
        for idx, x in enumerate(num):
            if x == '0' or x == '5':
                if idx == len(num)-1:
                    result = True
            else: break
        if result:
            answer.append(int(num))
            result = False
    if not(answer):
        answer.append(-1)
    return answer

# best solution
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]
