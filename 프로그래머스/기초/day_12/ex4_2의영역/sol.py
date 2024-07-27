# my solution
def solution(arr):
    answer = []
    lIndex = -1
    rIndex = -1
    for idx, x in enumerate(arr):
        if x == 2:
            if lIndex == -1:
                lIndex = idx
                rIndex = idx
            else:
                rIndex = idx
    answer = arr[lIndex:rIndex+1] if lIndex != -1 else [-1]
    return answer

# best solution
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
