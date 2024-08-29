# my solution
def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        answer = [x + n if idx % 2 == 0 else x  for idx, x in enumerate(arr)]
    else:
        answer = [x + n if idx % 2 == 1 else x  for idx, x in enumerate(arr)]
    return answer

# best solution
def solution(arr, n):
    N=len(arr)
    if N%2:
        for i in range(0,N,2): arr[i]+=n
    else:
        for i in range(1,N,2): arr[i]+=n
    return arr

