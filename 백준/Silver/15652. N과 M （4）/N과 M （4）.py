import sys
n, m = map(int, sys.stdin.readline().strip().split())
arr = []

def sol(start):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
    else:
        for i in range(start, n+1):
            arr.append(i)
            sol(i)
            arr.pop()
sol(1)