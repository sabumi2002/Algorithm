import sys
n = int(sys.stdin.readline().strip())
arr = [0][0]

def draw(n):
    if n <= 3:
        tmpArr = []
        for i in range(3):
            tmpArr.append([])
            for j in range(3):
                if (i == 1 and j == 1): tmpArr[i].append(' ')
                else: tmpArr[i].append('*')
        return tmpArr
    else:
        beforeArr = draw(n//3)
        afterArr = []
        for i in range(int(len(beforeArr))*3):
            afterArr.append([])
            afterArr[i] = beforeArr[i % int(len(beforeArr))] * 3
        for i in range(int(len(beforeArr)), int(len(beforeArr))*2):
            for j in range(int(len(beforeArr[i//3])), int(len(beforeArr[i//3]))*2):
                afterArr[i][j] = ' '
        return afterArr
            
arr = draw(n)
for i in range(n):
    print(''.join(arr[i]))