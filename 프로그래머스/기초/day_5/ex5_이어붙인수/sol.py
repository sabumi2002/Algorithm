# my solution
def solution(num_list):
    even = "".join([str(x) for x in num_list if x % 2 == 0])
    odd = "".join([str(x) for x in num_list if x % 2 == 1])
    answer = int(even)+int(odd)
    return answer

# best solution
def solution(num_list):
    return int(''.join([str(x) for x in num_list if x % 2])) + int(''.join([str(x) for x in num_list if not x % 2]))
