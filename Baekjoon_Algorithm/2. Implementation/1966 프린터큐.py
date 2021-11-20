test_case = int(input())
# 테스트 케이스 개수
for _ in range(test_case):
  a, b = map(int,input().split(" "))
  # a는 문서 개수, b는 몇번째로 인쇄되는지 궁금한 문서의 위치
  data = list(map(int,input().split(" ")))
  # 문서들의 중요도
  origin = list(range(a))
  # b번째가 타켓
  origin[b] = 'target'

  count = 0
  
  while(True):
    # 젤 앞에 있는 문서의 중요도가 가장 크면 count 증가
    if data[0] ==max(data):
      count += 1
      # 그게 타켓이면 몇번째로 인쇄되었는지 출력하고 끝.
      if(origin[0] == 'target'):
        print(count)
        break
      #타켓이 아니면 젤 앞에 있는 문서 삭제
      else:
        origin.pop(0)
        data.pop(0)
    else:
      #중요도가 최대가 아니면 젤 앞에 있는 문서 삭제하고 맨 뒤에 삽입
      origin.append(origin.pop(0))
      data.append(data.pop(0))