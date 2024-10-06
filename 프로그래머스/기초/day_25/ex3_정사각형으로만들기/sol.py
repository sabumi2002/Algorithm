arr = [[1, 2], [3, 4], [0]]
for i in range(len(arr)):
        for j in range(len(arr[i])):
            while len(arr) > len(arr[i]):
                arr[i].append(0)
        while (len(arr) < len(arr[i])):
             arr.append([0 for _ in range(len(arr[i]))])

print(arr)