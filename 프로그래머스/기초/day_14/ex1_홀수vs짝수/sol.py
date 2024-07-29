# my solution
def solution(num_list):
    answer = 0
    odd, even = [], []
    for idx, x in enumerate(num_list):
        if idx % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    odd = sum(odd)
    even = sum(even)
    answer = odd if odd >= even else even
    return answer


# best solution
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
