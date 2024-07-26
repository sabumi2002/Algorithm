# my solution
def solution(start_num, end_num):
    answer = [x for x in range(end_num, start_num+1)][::-1]
    return answer


# best solution
def solution(start, end):
    return list(range(start,end-1,-1))


