# my solution
def solution(x1, x2, x3, x4):
    def hap(x, y):
        if x==False and y==False:
            return False
        else: 
            return True
    def gop(x, y):
        if x==True and y==True:
            return True
        else:
            return False
    answer = gop(hap(x1, x2), hap(x3, x4))
    return answer

# best solution(1)
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)

# best solution(2)
solution=lambda w,x,y,z:(w or x)and(y or z)


