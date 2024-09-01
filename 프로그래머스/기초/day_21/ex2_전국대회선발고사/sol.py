# my solution
def solution(rank, attendance):
    attendance_rank = [x for idx, x in enumerate(rank) if attendance[idx]]
    attendance_rank.sort()
    a = rank.index(attendance_rank[0])
    b = rank.index(attendance_rank[1])
    c = rank.index(attendance_rank[2])
    answer = 10000 * a + 100 * b + c
    return answer

# best solution
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]

