# my solution
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1
    

# best solution
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer

