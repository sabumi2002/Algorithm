# my solution
def solution(ineq, eq, n, m):
    if eq == "=":
        if ineq == "<":
            answer = int(n <= m)
        else:
            answer = int(n >= m)
    else:
        if ineq == "<":
            answer = int(n < m)
        else:
            answer = int(n > m)
    return answer

# best solution
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
