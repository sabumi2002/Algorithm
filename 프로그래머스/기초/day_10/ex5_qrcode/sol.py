# my solution
q, r, code = 3, 1, "qjnwezgrpirldywt"
answer=""
for x in range(len(code)):
    if(x%q == r):
        answer += code[x]
print(answer)

# best solution
def solution(q, r, code):
    return code[r::q]

