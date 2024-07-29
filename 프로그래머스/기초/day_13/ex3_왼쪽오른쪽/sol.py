# my solution
def solution(str_list):
    for idx, x in enumerate(str_list):
        if x == "l":
            return str_list[:idx]
        if x == "r":
            return str_list[idx+1:]
    return []


# best solution


