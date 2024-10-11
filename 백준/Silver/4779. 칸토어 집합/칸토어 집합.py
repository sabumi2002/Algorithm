import sys
testList = list(map(int, sys.stdin.readlines()))
for n in testList:
    strLen = 3**n
    s = ['-' for _ in range(strLen)]

    def kanto(s):
        if len(s) >= 3:
            k, l = len(s)//3, len(s)//3*2
            for x in range(k, l):
                s[x] = ' '
            s[0:k] = kanto(s[0:k])
            s[l:len(s)] = kanto(s[l:len(s)])
        return s

    kanto(s)
    print(''.join(s))