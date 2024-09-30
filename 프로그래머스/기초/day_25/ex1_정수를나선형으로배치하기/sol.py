# my solution
def solution(n):
    def sol(answer, x, y, forwardNum, start):
        if start > n*n: return
        if answer[y][x] != 0: return
        answer[y][x] = start
        start += 1

        forward = wasd[forwardNum % 4]
        if forward == 'd':
            if x+1<n and answer[y][x+1] == 0:
                x = x + 1
            else:
                forwardNum += 1
                y = y + 1
            sol(answer, x, y, forwardNum, start)
        if forward == 's':
            if y+1<n and answer[y+1][x] == 0:
                y = y + 1
            else:
                forwardNum += 1
                x = x - 1
            sol(answer, x, y, forwardNum, start)
        if forward == 'a':
            if x-1>=0 and answer[y][x-1] == 0:
                x = x - 1
            else:
                forwardNum += 1
                y = y - 1
            sol(answer, x, y, forwardNum, start)
        if forward == 'w':
            if y-1>=0 and answer[y-1][x] == 0:
                y = y - 1
            else:
                forwardNum += 1
                x = x + 1
            sol(answer, x, y, forwardNum, start)


    wasd = ['d', 's', 'a', 'w']
    forwardNum = 0
    answer = [[0]*n for _ in range(n)]
    sol(answer, 0, 0, forwardNum, 1)
    return answer

# best solution
def solution(n):
    answer = [[None for j in range(n)] for i in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m + 1) % len(move)
        y, x = y + move[m][0], x + move[m][1]
    return answer
