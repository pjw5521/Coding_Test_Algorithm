# https://www.acmicpc.net/problem/1085
x, y, w, h = map(int,input().split())

answer = min(abs(x-0), abs(w-x), abs(y-0), abs(h-y))

print(answer)