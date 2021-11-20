n = input()

d = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in d:
  n = n.replace(i,"*")

print(len(n))