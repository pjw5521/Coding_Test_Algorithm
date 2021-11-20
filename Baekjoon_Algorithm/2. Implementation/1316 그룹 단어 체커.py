n = int(input())

result = n

for _ in range(n):
  word = input()
  for j in range(len(word)-1):
# 뒷 문자와 다르면 뒤에 해당 문자가 존재하는지 검사 
    if word[j] != word[j+1]:
      if word[j] in word[j+1:]:
        result -= 1
        break 

print(result)
