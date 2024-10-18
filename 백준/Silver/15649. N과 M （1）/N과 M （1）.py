import sys
n, m = map(int, sys.stdin.readline().strip().split())
arr = []

def sol(n, m, i):
    if int(len(arr)) >= m:
        print(" ".join(map(str, arr)))
    else:
        for j in range(1, n+1):
            if arr.count(j) <= 0:
                arr.append(j)
                sol(n, m, i+1)
                arr.pop()
sol(n, m, 1)