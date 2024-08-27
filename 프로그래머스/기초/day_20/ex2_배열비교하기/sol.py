# my solution
def solution(arr1, arr2):
    answer = 0
    if len(arr1) > len(arr2): answer = 1
    elif len(arr1) < len(arr2): answer = -1
    else:
        if sum(arr1) > sum(arr2): answer = 1
        elif sum(arr1) < sum(arr2): answer = -1
        else: 0
    return answer


# best solution
def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))



