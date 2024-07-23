# my solution
def solution(a, b, c, d):
    abcdArr = [a, b, c, d]
    abcdSet = set(abcdArr)
    answer = 0
    if len(abcdSet)==1:
        answer = 1111*abcdSet.pop()
    elif len(abcdSet)==2:
        p = abcdSet.pop()
        q = abcdSet.pop()
        if abcdArr.count(p) == 3 or abcdArr.count(q) == 3:
            if abcdArr.count(p) == 3:
                answer = (10*p+q)**2
            else:
                answer = (10*q+p)**2
        else:
            if (p-q) < 0:
                answer = (p+q)*(-1*(p-q))
            else:
                answer = (p+q)*(p-q)
    elif len(abcdSet)==3:
        p = 0
        for x in abcdSet:
            if abcdArr.count(x) == 2:
                p = x
        abcdSet.remove(p)
        q = abcdSet.pop()
        r = abcdSet.pop()
        answer = q*r
    else:
        answer = sorted(abcdArr)[0]
    return answer

# best solution
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)

