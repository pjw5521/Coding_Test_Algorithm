# 자주 쓰이는 문법 정리 

## 리스트 정렬
- sort() : 기본값 오름차순 정렬, reverse = True 시 내림차순 정렬
    + 정렬 기준 값 설정 : m.sort(key=lambda x : (기준값1, 기준값 2, .. ))
- reverse() : 리스트 거꾸로 뒤집어서 정렬

## 순열과 조합 
- 순열 : from itertools import permutations 
    + ex) permute = list(permutations(data,m))
- 조합 : from itertools import combinations
    + ex) combine = list(combinations(data,m))
- 중복 순열 : from itertools import product
    + ex) product = list(product(data,repeat = m ))
- 중복 조합 : from itertools import combinations_with_replacement
    + ex) ex ) combine = list(combinations_with_replacement(data,m))