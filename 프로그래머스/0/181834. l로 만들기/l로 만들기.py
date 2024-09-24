def solution(myString):
    answer = "".join(["l" if x < "l" else x for x in myString])
    return answer