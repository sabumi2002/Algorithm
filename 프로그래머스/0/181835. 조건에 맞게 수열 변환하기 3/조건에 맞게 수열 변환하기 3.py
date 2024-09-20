def solution(arr, k):
    answer = [x+k if k % 2 == 0 else x*k for x in arr]
    return answer