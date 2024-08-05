# my solution
from functools import reduce
def solution(num_list):
    def func(x, y):
        return x*y
    answer = sum(num_list) if len(num_list) >= 11 else reduce(func, num_list)
    return answer

# best solution (1)
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))
# eval() 
# best solution (2)
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)
