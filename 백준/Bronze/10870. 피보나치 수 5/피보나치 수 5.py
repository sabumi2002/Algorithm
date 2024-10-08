import sys
n = int(sys.stdin.readline().rstrip())
def fibo(n):
    res = 0
    if n > 1:
        res= fibo(n-1) + fibo(n-2)
    elif n == 1:
        res=1
    else:
        res=0
    return res
print(fibo(n))