# my solution
def solution(my_string):
    answer = sorted([my_string[-idx:] for idx in range(len(my_string))])
    return answer

# best solution

