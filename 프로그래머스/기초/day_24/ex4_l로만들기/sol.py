# my solution
def solution(myString):
    answer = "".join(["l" if x < "l" else x for x in myString])
    return answer


# best solution
def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

# translate 문자만 변환 (dictionary를 통해 1대1로 문자열을 변환)
# maketrans 문자열 치환 (변환 dictionary)
