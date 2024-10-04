def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            while len(arr) > len(arr[i]):
                arr[i].append(0)
        while (len(arr) < len(arr[i])):
             arr.append([0 for _ in range(len(arr[i]))])
    return arr