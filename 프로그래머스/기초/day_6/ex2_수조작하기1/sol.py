# my solution
def solution(n, control):
    wasd = {"w": 1, "s": -1, "d": 10, "a": -10}
    for x in control:
        n += wasd[x]
    return n

# best solution
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])

