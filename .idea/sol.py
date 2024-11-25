# import sys
# n = int(sys.stdin.readline().strip())
import copy
n = int(input())

square = [[0]*n  for _ in range(n)]
count = 0

def print2(square):
    for i in range(n):
        print(square[i])
    print()

def sol(start, square):
    global count
    if (start == n):
        return
    v = [row[:] for row in square]
    for j in range(n):
        if(v[start][j] == 0):
            if (start == n-1):
                count += 1
                print2(v)
                print(count)
            for k in range(n):
                v[k][j] = 1
            for k in range(n):
                v[start][k] = 1
            for k in range(n):
                if (start-k >= 0 and j-k >= 0):
                    v[start-k][j-k] = 1
            for k in range(start, -1, -1):
                if (start-k >= 0 and j+k < n):
                    v[start-k][j+k] = 1
            for k in range(start, n):
                if (start+k < n and j+k < n):
                    v[start+k][j+k] = 1
            for k in range(start, n):
                if (start+k < n and j-k >= 0):
                    v[start+k][j-k] = 1
  
            print(start, j)
            print2(v)
            sol(start+1, v)
            v = [row[:] for row in square]
sol(0, square)
print(count)

