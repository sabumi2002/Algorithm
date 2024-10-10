import sys
def merge_sort(A, p, r, req, count):
    answer = 0
    if (p < r):
        q = (p+r)//2
        count, answer = merge_sort(A, p, q, req, count)
        if req == count: return count, answer
        count, answer = merge_sort(A, q + 1, r, req, count)
        if req == count: return count, answer
        count, answer = merge(A, p, q, r, req, count)
        if req == count: return count, answer
        return count, -1
    return count, -1

def merge(A, p, q, r, req, count):
    i, j, t = p, q+1, 0
    tmp = [0]
    while (i <= q and j <= r):
        if (A[i] <= A[j]):
            tmp.append(A[i])
            t += 1
            i += 1
        else:
            tmp.append(A[j])
            t += 1
            j += 1
    while (i <= q):
        tmp.append(A[i])
        t += 1
        i += 1
    while (j <= r):
        tmp.append(A[j])
        t += 1
        j += 1
    i, t = p, 1
    while (i <= r):
        count += 1
        if req == count: return count, tmp[t]
        A[i] = tmp[t]
        i += 1
        t += 1
    return count, 0

n, req = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
count = 0
count, answer = merge_sort(arr, 0, int(len(arr)-1), req, count)
print(answer)