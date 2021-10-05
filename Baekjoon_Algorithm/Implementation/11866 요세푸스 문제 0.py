a, b = map(int,input().split(" "))

# pop() 맨마지막 요소 꺼내고 삭제
# pop(x) x 번째 요소 꺼내고 삭제

data = [i for i in range(1,a+1)]
num = 0
result = []
for i in range(a):
  num += b-1 
  if num >= len(data):
    num = num % len(data)
  result.append(str(data.pop(num)))

# .join(list)는 list의 문자열 하나로 합침
# 구분자.join(list)는 구분자 넣어서 문자열 하나로 합침 
print("<%s>" %", ".join(result))