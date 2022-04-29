# https://www.acmicpc.net/problem/1914
import sys
input = sys.stdin.readline

def hanoi(n, From, To, Sub):
    if n == 1 :
        answer.append((From,To))
        return 
        
    # From에 있는 n-1 개의 원반을 To를 거쳐 Sub로 옮기기
    hanoi(n-1, From, Sub, To)
    # From에 있는 하나의 원반을 To로 옮기기
    answer.append((From, To))
    # Sub로 옮긴 n-1개의 원반을 From을 거쳐 To로 옮기기 
    hanoi(n-1, Sub, To, From)
    
n = int(input())
answer = []

# n이 20 이하일 때만 실행 
if n <= 20:
    hanoi(n,1,3,2)
    print(len(answer))
    for i in answer:
        print(*i)
else:
    print(2**(n-1))