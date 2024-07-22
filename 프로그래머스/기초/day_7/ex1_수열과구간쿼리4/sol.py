# my solution
arr, queries = [0, 1, 2, 4, 3], [[0, 4, 1],[0, 3, 2],[0, 3, 3]]
for s, e, k in queries:
    for i, x in enumerate(arr[s:e+1]):
        print(f'{i}, {x}')
        if i%k == 0:
            arr[i] += 1
for s, e, k in queries:
    for i in range(s, e+1):
        print(i)
        if i%k == 0:
            arr[i] += 1
print(arr)

print(arr)
# best solution

