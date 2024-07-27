# my solution
def solution(arr, query):
    for idx, x in enumerate(query):
        if idx %2==0:
            arr = arr[:x+1]
        else:
            arr = arr[x:]
    return arr


# best solution


