# my solution
binomial = "43 + 12"
a, op, b = binomial.split(' ')

if op == '+':
    answer = int(a) + int(b)
elif op == '-':
    answer = int(a) - int(b)
elif op == '*':
    answer = int(a) * int(b)

print(answer)


# best solution



