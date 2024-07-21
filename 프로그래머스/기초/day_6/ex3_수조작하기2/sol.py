# my solution 
def solution(numLog):
    wsda = {"w": 1, "s": -1, "d":10, "a":-10}
    wsda = {v: k for k, v in wsda.items()}
    answer = "".join([wsda[numLog[idx]-numLog[(idx-1)]] for idx, x in enumerate(numLog) if idx >0])
    return answer

# best solution
def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res

