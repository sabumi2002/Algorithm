# bfs 인접행렬 + queue
n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1

from collections import deque

def bfs(matrix, i, visited):
    queue = deque()
    queue.append(i)
    while queue:
        value = queue.popleft()
        # 방문한적이 없으면 방문하고 방문체크
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True
            # 인접행렬 구현은 matrix 행마다 모든 열을 검사한다.
            for c in range(len(matrix[value])):
                if matrix[value][c] == 1 and not visited[c]:
                    queue.append(c)


# bfs 인접리스트 + queue