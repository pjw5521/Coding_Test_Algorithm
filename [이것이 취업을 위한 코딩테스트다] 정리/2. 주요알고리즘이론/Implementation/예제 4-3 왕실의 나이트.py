n = input()

row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1 

data = [(-2, -1), (-2, +1), (+2, +1), (+2, -1), (+1, +2), (-1, +2), (+1, -2), (-1, -2)]

count = 0
for i in data:
  next_row = row + i[0]
  next_column = column + i[1]

  if next_column >= 1 and next_row >= 1 and next_column <= 8 and next_row <= 8:
    count += 1

print(count)