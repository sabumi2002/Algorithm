# my solution
import sys
n = int(sys.stdin.readline().strip())
result= str(n) + ' is even' if n % 2 == 0 else str(n) + ' is odd'
print(result)

# best solution
N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")