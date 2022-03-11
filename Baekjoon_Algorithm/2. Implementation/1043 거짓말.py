# https://www.acmicpc.net/problem/1043
n, m = map(int,input().split())

s = input().split()

# 진실을 아는 사람 
truth = set()

for i in range(1,int(s[0])+1):
  truth.add(s[i])

# 파티에 참석하는 사람들 집합의 리스트 
party = []
# 과장할 수 있는지 여부 기록 
possible = []

# 파티에 참석하는 사람들 집합을 리스트에 추가
for _ in range(m):
  people = input().split()

  party.append(set(people[1:]))
  possible.append(1)

# 파티의 개수만큼 반복해서 검증 
for _ in range(m):
  for i in range(m):
    # 진실을 아는 사람, 증인들과 교집합이 존재한다면 
    if truth.intersection(party[i]):
      # 과장할 수 없음 기록 
      possible[i] = 0
      # truth 집합에 증인들까지 추가 
      truth = truth.union(party[i])

print(sum(possible))