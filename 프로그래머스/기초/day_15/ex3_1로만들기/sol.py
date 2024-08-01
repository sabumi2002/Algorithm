# my solution
def solution(num_list):
    list_count = [0 for _ in range(len(num_list))]
    while max(num_list)>1:
        for idx in range(len(num_list)):
            if num_list[idx] <= 1:
                continue
            elif num_list[idx] % 2 ==0:
                list_count[idx] += 1
                num_list[idx] //=2
            elif num_list[idx] % 2 == 1:
                list_count[idx] += 1
                num_list[idx] //=2
    answer = sum(list_count)
    return answer

# best solution (1)
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)

# best solution (2)
def solution(num_list):
    answer = 0
    for n in num_list:
        while n != 1:
            n //= 2
            answer += 1
    return answer
