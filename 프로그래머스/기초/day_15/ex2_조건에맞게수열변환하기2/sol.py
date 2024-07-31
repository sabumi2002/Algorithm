# my solution
def solution(arr):
    temp = []
    def arrFunc(arr):
        for idx in range(len(arr)):
            if arr[idx]>=50 and arr[idx]%2==0:
                arr[idx] = arr[idx] // 2
            elif arr[idx]<50 and arr[idx]%2==1:
                arr[idx] = arr[idx]*2 + 1 
        return arr
    answer = -1

    while arr != temp:
        temp = arr[:]
        arrFunc(temp)
        answer += 1
        if arr != temp:
            arr = temp[:]
            temp = []
    return answer

# best solution
def solution(arr):
    answer = 0
    old = arr
    while(True):
        new = []
        for i in old:
            if i>=50 and i%2 == 0:
                i = i/2
            elif i<50 and i%2 == 1:
                i = i*2 + 1
            new.append(int(i))
        if old == new:
            break
        else:
            old = new
            answer += 1
    return answer

