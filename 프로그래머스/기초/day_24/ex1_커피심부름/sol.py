# my solution
def solution(order):
    def orderProc(order):
        orderSet = {"americano":4500, "latte":5000}
        result = 4500
        for x, y in orderSet.items():
            if x in order:
                result = y
                break
        return result
    answer = 0
    for x in order:
        answer += orderProc(x)
    return answer

# best solution
def solution(order):
    answer = 0
    for want in order:
        if 'latte' in want:
            answer += 500
        answer += 4500

    return answer

# sry

