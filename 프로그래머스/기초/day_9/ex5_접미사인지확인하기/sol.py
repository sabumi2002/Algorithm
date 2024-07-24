# my solution
def solution(my_string, is_suffix):
    suffixList = [my_string[-idx:] for idx in range(len(my_string))]
    answer = int(is_suffix in suffixList)
    return answer

# best solution (1)
def solution(m, s):
    if m[-len(s):]==s: return 1
    return 0

# best solution (2)
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))