# my solution
def solution(my_string, indices):
    answer = [x for x in my_string]
    for idx in indices:
        answer[idx]= ' '
    answer = ''.join(answer).replace(' ', '')
    return answer

# best solution (1)
def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer

# best solution (2)
def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_string[i]
    return ''.join(my_string)

