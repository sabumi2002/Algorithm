# my solution
import sys
str = sys.stdin.readline().strip()
for x in str:
    print(x)

# best solution (1)
print('\n'.join(input()))
# best solution (2)
print(*[x for x in input()], sep='\n')