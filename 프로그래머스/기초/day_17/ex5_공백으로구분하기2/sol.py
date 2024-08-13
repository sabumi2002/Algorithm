# my solution
def solution(my_string):
    answer = [x for x in my_string.strip().split(' ') if x not in '']
    return answer


# best solution (1)
solution=lambda x:x.split()

# best solution (2)
def solution(my_string):
    answer = my_string.split()
    return answer


