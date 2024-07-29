# my solution
def solution(todo_list, finished):
    answer = [todo_list[idx] for idx in [idx for idx, x in enumerate(finished) if x == False]]
    return answer


# best solution (1)
def solution(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]

# best solution (2)
def solution(todo_list, finished):
    return [x for x, b in zip(todo_list, finished) if not b]
