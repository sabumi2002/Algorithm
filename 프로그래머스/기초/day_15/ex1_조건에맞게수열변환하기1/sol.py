# my solution
def solution(arr):
    for idx in range(len(arr)):
        if arr[idx]>=50 and arr[idx]%2==0:
            arr[idx] = arr[idx]//2
        elif arr[idx]<50 and arr[idx]%2==1:
            arr[idx] = arr[idx]*2
    return arr


# best solution
def solution(arr):
    for i in range(len(arr)):
        x=arr[i]
        if x>=50 and not x%2: arr[i]//=2
        elif x<50 and x%2: arr[i]*=2
    return arr


