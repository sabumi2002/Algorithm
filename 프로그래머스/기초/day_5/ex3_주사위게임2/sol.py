# my solution
def solution(a, b, c):
    answer = 0
    numArr = []
    if not(a in numArr): numArr.append(a)
    if not(b in numArr): numArr.append(b)
    if not(c in numArr): numArr.append(c)
    if len(numArr) == 3:
        answer = a+b+c
    elif len(numArr) == 2:
        answer = (a+b+c)*(a**2+b**2+c**2)
    elif len(numArr) == 1:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    return answer

# best solution
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)
