import sys

def factorial(n):
    if n > 1:
        n *= factorial(n-1)
    else:
        n = 1
    return n

n = int(sys.stdin.readline().rstrip())

print(factorial(n))