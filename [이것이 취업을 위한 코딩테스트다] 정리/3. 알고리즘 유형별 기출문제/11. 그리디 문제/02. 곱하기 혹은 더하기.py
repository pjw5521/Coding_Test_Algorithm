# 문제 312쪽
data = input()

result = 0
for i in data:
  num = int(i)
  if result == 0:
    result += num
  elif num == 0 or num == 1 :
    result += num
  else:
    result *= num

print(result)