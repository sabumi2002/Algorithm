# my solution
def solution(arr):
    num = 1
    while len(arr) > num:
        if len(arr) == 0:
            num = 0
        elif len(arr) == 1:
            num = 1
        else:
            num *= 2
    for _ in range(num - len(arr)):
        arr += [0]
    return arr


# best solution
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)


"""
2의 거듭제곱 확인 방법 O(1)로 해야 겨우 O(n)
logn으로 확인하면 그걸 n번 반복 -> o(nlogn)
길이 1000개 -> 가장 빠른방법은 각각 하드코딩하기 겨우 10개

"""


