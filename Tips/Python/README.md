# 파이썬 Tip

## 자료형

- 리스트 컴프리헨션
    
    ```python
    # 0부터 19까지의 수 중에서 홀수만 포함하는 리스트 (1)
    array = [i for i in range(20) if i % 2 == 1]
    
    # 0부터 19까지의 수 중에서 홀수만 포함하는 리스트 (2)
    array = []
    	for i in range(20):
    		if i % 2 == 1:
    			array.append(i)
    			
    # 2차원 리스트 초기화 (n*m 크기)
    array = [[0] * m for _ in range(n)]
    
    # 리스트에서 특정 값을 가지는 원소를 모두 제거하기
    # a라는 리스트를 i라는 변수가 하나씩 확인하면서 i라는 변수가 remove_set에 포함되어있지 않다면 그원소만 남겨놓겠다.
    a = [1, 2, 3, 4, 5, 5, 5]
    remove_set = {3, 5}
    result = [i for i in a if i not in remove_set]
    ```
    
- 문자열 슬라이싱
    
    ```python
    a = "ABCDEF"
    print(a[2 : 4])
    ```
    
- 실수형 자료 연산 시
    - round() 함수를 이용해 반올림하여 계산한다. (컴퓨터는 10진수를 제대로 표현하지 못하기 때문)
        
        ```python
        # 123.456을 소수 셋째 자리에서 반올림
        round(123.456, 2)
        
        # 결과
        123.46
        ```
        
- 수 자료형의 연산
    - 나누기 연산자(/)는 나눠진 결과를 실수형으로 반환한다.
    - 나머지 연산자(%), 몫 연산자(//), 거듭제곱 연산자(**)
- 튜플을 사용하면 좋은 경우
    - 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
        - 최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용합니다.
    - 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
        - 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있습니다.
    - 리스트보다 메모리를 효율적으로 사용해야 할 때

## 사전, 집합 자료형

- 사전 자료형
    - 사전 자료형은 키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형입니다.
        - 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됩니다.
    - 사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 ‘변경 불가능한(Immutable) 자료형’을 키로 사용할 수 있습니다.
    - 파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.
        
        ![Untitled](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20Tip%2069227f1150c044688e79b612602d6477/Untitled.png)
        
        ![Untitled](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20Tip%2069227f1150c044688e79b612602d6477/Untitled%201.png)
        

- 사전 자료형과 집합 자료형의 특징
    - 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있습니다.
    - 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없습니다.
        - 사전의 키(Key) 혹은 집합의 원소(Element)를 이용해 O(1)의 시간 복잡도로 조회합니다.
- 집합 자료형
    - 집합은 다음과 같은 특징이 있습니다.
        - 중복을 허용하지 않습니다.
        - 순서가 없습니다.
    - 집합은 리스트 혹은 문자열을 이용해서 초기화할 수 있습니다.
        - 이때 set() 함수를 이용합니다.
    - 혹은 중괄호 ({})안에 각 원소를 콤마(,)를 기준으로 구분하여 삽입함으로써 초기화 할 수 있습니다.
    - 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.
    - 
    
    ```python
    # 집합 자료형 초기화 방법 1
    data = set([1, 1, 2, 3, 4, 4 ,5])
    print(data)
    # 집합 자료형 초기화 방법 2
    data = {1, 1, 2, 3, 4, 4, 5}
    print(data)
    # 실행 결과
    {1, 2, 3, 4, 5}
    {1, 2, 3, 4, 5}
    
    ------------------------------
    # 집합 자료형 관련함수
    data = set([1, 2 ,3])
    print(data)
    # 새로운 원소 추가
    data.add(4)
    print(data)
    # 새로운 원소 여러 개 추가
    data.update([5, 6])
    print(data)
    # 특정한 값을 갖는 원소 삭제
    data.remove(3)
    print(data)
    # 실행 결과
    {1, 2, 3}
    {1, 2, 3, 4}
    {1, 2, 3 ,4, 5, 6}
    {1, 2, 4, 5, 6}
    
    -------------------------------
    # 집합 자료형의 연산
    a = set([1, 2 ,3 4, 5])
    b = set([3, 4, 5, 6, 7])
    # 합집합
    print(a | b)
    # 교집합
    print(a & b)
    # 차집합
    print(a - b)
    # 실행 결과
    {1, 2 ,3 ,4 ,5 ,6 ,7}
    {3, 4, 5}
    {1, 2]
    ```
    

## 입출력

- 빠르게 입력 받기
    
    ```python
    import sys
    
    data = sys.stdin.readline().rstrip()
    print(data)
    ```
    
- 출력을 위한 전형적인 소스코드
    
    ```python
    # 출력할 변수들
    a = 1
    b = 2
    print(a, b)
    print(7, end=" ")
    print(8, end=" ")
    
    # 출력할 변수
    answer = 7
    print("정답은 " + str(answer) + "입니다. ")
    
    # 실행 결과
    1 2
    7 8 정답은 7입니다.
    ```
    
- f-string // 파이썬 3.6 부터 사용 가능
    
    ```python
    answer = 7
    print(f"정답은 {answer}입니다.")
    
    # 실행 결과
    정답은 7입니다.
    ```
    
- 자주 사용되는 표준 입력 방법
    - input() 함수는 한 줄의 문자열을 입력 받는 함수입니다.
    - map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용합니다.
    - 예시) 공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용합니다.
        - list(map(int, input().split()))
    - 예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용합니다.
        - a, b, c = map(int, input().split())
- 입력을 위한 전형적인 소스코드

```python
# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)

# 실행 결과
5
65 90 75 34 99
[99, 90, 75, 65, 34]
```

## 반복문, 조건문 간소화

- 반복문: for문
    - 반복문으로 for문을 이용할 수도 있습니다.
    - for문의 구조는 다음과 같은데, 특정한 변수를 이용하여 ‘in’ 뒤에 오는 데이터(리스트, 튜플 등)에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문합니다.
        
        ```python
        for 변수 in 리스트:
        	실행할 소스코드
        ```
        
- 조건문의 간소화
    - 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있습니다.
        
        ```python
        score = 85
        
        if score >= 80: result = "Success"
        else: result = "Fail"
        
        # 실행 결과
        Success
        ```
        
    - 조건부 표현식(Conditional Expression)은 if ~ else문을 한 줄에 작성할 수 있도록 해줍니다.
    
    ```python
    score = 85
    result = "Success" if score >= 80 else "Fail"
    
    print(result)
    
    # 실행 결과
    Success
    ```
    

## 함수

## 람다식

## 라이브러리