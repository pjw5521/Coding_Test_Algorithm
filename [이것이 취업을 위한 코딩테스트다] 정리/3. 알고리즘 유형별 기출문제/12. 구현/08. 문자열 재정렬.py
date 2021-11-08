# 문제 322쪽 
s = input()

alpha = []
result = 0 
for i in s:
  if i.isalpha():
    alpha.append(i)
  else:
    result += int(i)


alpha.sort()

print("".join(alpha), end ="")
print(result)