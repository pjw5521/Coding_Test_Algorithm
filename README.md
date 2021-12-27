# Coding_Test_Algorithm

## 참고한 책 
이것이 취업을 위한 코딩테스트다 with 파이썬_한빛미디어, 나동빈 저자 


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

## 사용한 함수 모음 
- zfill(n) : 자리수가 n이 되도록 앞에 0 추가
- "".join(n) : 배열의 값 사이에 ""안에 들어있는 문자를 추가해서 출력 
- isdigit(), isalpha() 
- upper(), lower()
- count()