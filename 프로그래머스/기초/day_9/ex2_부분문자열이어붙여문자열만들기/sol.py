# my solution
def solution(my_strings, parts):
    answer = ''
    for idx, part in enumerate(parts):
        answer += my_strings[idx][part[0]:part[1]+1]
    return answer

# best solution
def solution(my_strings, parts):
    answer = ''
    for s, (x, y) in zip(my_strings, parts):
        answer += s[x:y+1]
    return answer
