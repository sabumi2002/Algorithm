# my solution
def solution(arr, queries):
    for query in queries:
        temp = arr[query[0]]
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = temp
    return arr


# best solution
def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr

