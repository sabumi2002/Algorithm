# my solution
def solution(str_list, ex):
    answer = "".join([x for x in str_list if ex not in x])
    return answer

# best solution
def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))
