# Coding_Test_Algorithm

## 참고한 책 
이것이 취업을 위한 코딩테스트다 with 파이썬_한빛미디어, 나동빈 저자 

## 문제 풀이 사이트 
- 백준 : https://www.acmicpc.net
- 프로그래머스 : https://programmers.co.kr

## 자주 쓰이는 문법 정리 

### 리스트 정렬
- sort() : 기본값 오름차순 정렬, reverse = True 시 내림차순 정렬
    + 정렬 기준 값 설정 : m.sort(key=lambda x : (기준값1, 기준값 2, .. ))
- reverse() : 리스트 거꾸로 뒤집어서 정렬

### 순열과 조합 
- 순열 : from itertools import permutations 
    + ex) permute = list(permutations(data,m))
- 조합 : from itertools import combinations
    + ex) combine = list(combinations(data,m))
- 중복 순열 : from itertools import product
    + ex) product = list(product(data,repeat = m ))
- 중복 조합 : from itertools import combinations_with_replacement
    + ex) ex ) combine = list(combinations_with_replacement(data,m))

### deque
- from collections import deque
    + append() : 왼쪽에 추가
    + appendleft() : 오른쪽에 추가 
    + pop() : 제일 오른쪽 data 꺼내기
    + popleft() : 제일 왼쪽 data 꺼내기
    + len(q) : 큐 사이즈 
    
## enumerate 함수 
-  리스트의 순서와 값을 전달하는 함수 

## dictionary 
- key와 value를 한 쌍으로 가지는 자료형 : { key1 : value1, key2 : value2, ... }
- 정렬 : sorted 사용 
    + sorted(dic, key = lambda x : dic[x]) : value값 기준으로 정렬 후 key 반환 
    + dict(sorted(dic, key = lambda x : (x[0],x[1]))): key, value 모두 기준으로 사용 시 
- defaultdict() : 기본값이 있는 딕셔너리 
    + from collections import defaultdict
    + defaultdict()은 인자로 주어진 객체의 기본값을 딕셔너리의 초깃값으로 지정 가능
    + int, list, set 등으로 초기화 가능
    + 예를 들어 defaultdict(int)일 경우, 값을 지정하지 않은 키는 그 값이 0으로 지정 
    
## 사용한 함수 모음 
- zfill(n) : 자리수가 n이 되도록 앞에 0 추가
- "".join(n) : 배열의 값 사이에 ""안에 들어있는 문자를 추가해서 출력 
    + int일 경우 str로 변환해서 출력해야 함 : "". join(map(str,n))
- isdigit() : 숫자인지 판별 
- isalpha() : 영어 또는 한글로만 이루어져 있는지 확인. 공백, 특수문자, 숫자가 포함되어 있으면 False 
- upper(), lower() : 소문자, 대문자 변환 
- count() : 개수 반환 
- zip(,) : 객체를 인자로 받고, 각 객체가 담고 있는 원소들을 튜플의 형태로 차례대로 접근할 수 있는 반복자를 반환 
    ```python
    # 예시 
    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]
    for pair in zip(numbers, letters):
        print(pair)
    (1, 'A')
    (2, 'B')
    (3, 'C')
    ```
- remove(a) : 리스트에서 a원소 제거
- Counter(a) : 리스트에서 등장하는 알파벳을 key, 개수를 value로 하는 딕셔너리 반환 
    + from collections import Counter
- discard(a), remove(a) : set에서 원소 삭제.
    + discard는 집합에 a라는 원소가 없어도 에러 발생 x, remove는 에러 발생 o 
- ord(문자), chr(숫자) : 문자, 숫자의 아스키 코드 반환 
- bin(숫자), oct(숫자), hex(숫자) : 2진수, 8진수, 16진수 변환

## 힙 자료구조
- 최소 힙 자료구조 제공 
    + 원소들이 항상 정렬된 상태로 추가되고, 삭제 
    + 가장 작은 원소가 제일 앞에 추가
    + 가장 작은 원소가 제일 먼저 삭제 
- import heapq
- 원소 추가 : heapq.heappush( 리스트 이름, 원소 )
- 원소 삭제 : heapq.heappop( 리스트 이름 ) 

## 스택 자료구조 
- 가장 나중에 들어온 자료가 가장 먼저 처리되는 *LIFO(Last-In-First-Out)* 자료구조 
- init : 리스트로 스택을 흉내 
    ```python
    # 예시 
    stack = []
    ```
- push : append 메소드로 리스트의 가장 마지막에 추가 
- pop : pop 메소드로 리스트의 가장 마지막 원소 제거후 제거된 원소 반환 
    + pop(index)는 해당 인덱스의 원소 삭제한 뒤 삭제한 원소 반환 
- 스택에서 원소를 제거하지 않고 그냥 가져오기만 할 때는 [-1] 이용 
    ```python
    # 예시 
    top = stack[-1]
    ```