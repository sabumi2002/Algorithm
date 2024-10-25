import sys
n, m = map(int, sys.stdin.readline().strip().split())
arr = []
v = []

def sol(arr, n, m):
    if int(len(arr)) >= m:
        check = False
        count = 0
        for y in v:
            if count >= m:
                check = True
                break
            count = 0
            for z in y:
                for x in arr:
                    if z == x:
                        count += 1
        if count >= m:
                check = True    

        if check == False:
            v.append(arr)
            print(" ".join(map(str, arr)))
        
    else:
        for j in range(1, n+1):
            if arr.count(j) <= 0:
                tmpArr = [*arr]
                tmpArr.append(j)
                sol(tmpArr, n, m)
    
sol(arr, n, m)