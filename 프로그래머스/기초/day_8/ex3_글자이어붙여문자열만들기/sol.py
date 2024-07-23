# my solution
def solution(my_string, index_list):
    answer = "".join([my_string[x] for x in index_list])
    return answer


# best solution
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])

