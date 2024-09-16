# my solution
def solution(date1, date2):
    answer = 0
    for x in range(3):
        if (date1[x] < date2[x]):
            answer = 1
            break
        if (date1[x] > date2[x]):
            answer = 0
            break
    return answer

# best solution (1)
def solution(date1, date2):
    return int(date1 < date2)

