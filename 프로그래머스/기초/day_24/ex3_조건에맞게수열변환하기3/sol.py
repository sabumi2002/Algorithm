# my solution
arr, k = [1, 2, 3, 100, 99, 98], 3
answer = [x+k if k % 2 == 0 else x*k for x in arr]
print(answer)


# best solution
def solution(arr, k):
    if k % 2 != 0:
        return list(map(lambda x: x * k, arr))

    return list(map(lambda x: x + k, arr))
