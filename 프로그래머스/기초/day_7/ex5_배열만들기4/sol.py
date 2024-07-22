# my solution
def solution(arr):
    i = 0
    stk=[]
    while i<len(arr):
        if not(stk):
            stk.append(arr[i])
            i+=1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i+=1
            elif stk[-1] >= arr[i]:
                stk.pop()
    return stk

# best solution
def solution(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk
