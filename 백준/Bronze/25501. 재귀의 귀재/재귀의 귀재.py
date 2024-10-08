import sys
def recursion(s, l, r, count):
        count += 1
        if(l >= r): return 1, count
        elif (s[l] != s[r]): return 0, count
        else: return recursion(s, l+1, r-1, count)
def isParlindrome(s):
    count = 0
    return recursion(s, 0, len(s)-1, count)

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    answer, count = isParlindrome(s)
    print(f"{answer} {count}")