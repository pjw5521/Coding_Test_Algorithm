# https://www.acmicpc.net/problem/2447
def draw(n):
    if n == 1 :
        return ['*']
    stars = draw(n//3)
    tmp = []
    for s in stars:
        tmp.append(s*3)
    for s in stars:
        tmp.append(s+" "*(n//3) + s)
    for s in stars:
        tmp.append(s*3)
    
    return tmp

n = int(input())

answer = draw(n)
for i in answer:
    print("".join(i))