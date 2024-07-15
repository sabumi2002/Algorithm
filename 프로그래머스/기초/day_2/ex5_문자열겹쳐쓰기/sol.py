# my solution
import sys
my_string, overwrite_string, s = map(str, sys.stdin.readline().strip().split())
result = my_string[0:int(s)]+overwrite_string+my_string[int(s)+len(overwrite_string):]
print(result)
