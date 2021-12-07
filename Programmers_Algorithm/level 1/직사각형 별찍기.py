# https://programmers.co.kr/learn/courses/30/lessons/12969
a, b = map(int, input().strip().split(' '))
result = [ '*' * a for _ in range(b)]
for i in result :
    print("".join(i))