# my solution
def solution(num_list):
    result = 1
    for x in num_list:
        result *= x
    answer = 1 if result<sum(num_list)**2 else 0
    return answer

# best solution (1)
from functools import reduce
def solution(num_list):
    return 1 if (reduce(lambda x, y: x * y, num_list)) < (sum(num_list) ** 2) else 0

# best solution (2)
import math
def solution(num_list):
    answer = 0
    if math.prod(num_list) < (sum(num_list)**2):
        answer = 1
    return answer
