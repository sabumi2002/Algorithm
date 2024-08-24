# my solution
def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) != 0 and stk[-1] == arr[i]:
            stk.pop()
            i += 1
        elif len(stk) != 0 and stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    stk = [-1] if len(stk) == 0 else stk
    return stk

# best solution
def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]
