# my solution
def solution(my_string, is_prefix):
    prefixList = [my_string[:x] for x in range(len(my_string))]
    answer = int(is_prefix in prefixList)
    return answer

# best solution (1)
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

# best solution (2)
def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)]==is_prefix:return 1
    return 0

# best solution (3)
def solution(my_string, is_prefix):
    return 1 if my_string.find(is_prefix) == 0 else 0

