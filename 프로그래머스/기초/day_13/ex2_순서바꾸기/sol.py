# my solution
def solution(num_list, n):
    answer = num_list[n:]+num_list[:n]
    return answer

# best solution
def solution(num_list, n):
    if not isinstance(num_list, list) : raise TypeError(num_list)
    if not isinstance(n, int) : raise TypeError(n)

    if not (2 <= len(num_list) <= 30) : raise ValueError(num_list)
    if not (1 <= n <= len(num_list)) : raise ValueError(num_list, n)

    if not all(isinstance(num, int) for num in num_list) : raise TypeError(num_list)
    if not all(1 <= num <= 9 for num in num_list) : raise ValueError(num_list)

    return num_list[n:] + num_list[:n]


