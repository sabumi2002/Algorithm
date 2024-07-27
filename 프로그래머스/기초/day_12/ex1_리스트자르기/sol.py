# my solution
def solution(n, slicer, num_list):
    if n==1:
        return num_list[0:slicer[1]+1]
    elif n==2:
        return num_list[slicer[0]:]
    elif n==3:
        return num_list[slicer[0]:slicer[1]+1]
    elif n==4:
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]

# best solution

def solution(n, slicer, num_list):
    a, b, c = slicer
    return [num_list[:b + 1], num_list[a:], num_list[a:b + 1], num_list[a:b + 1:c]][n - 1]


