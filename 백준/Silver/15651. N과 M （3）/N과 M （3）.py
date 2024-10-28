import sys
n, m = map(int, sys.stdin.readline().strip().split())
arr = []

def sol(n, m):
    if len(arr) >= m:
        print(" ".join(map(str, arr)))
    else:
        for i in range(1, n+1):
            arr.append(i)
            sol(n, m)
            arr.pop()
sol(n, m)