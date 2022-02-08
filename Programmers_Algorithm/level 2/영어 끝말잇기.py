# https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
  answer = []
  
  # 끝말잇기에 등장한 단어 저장 
  word = set()
  # 전 단어의 마지막 알파벳 저장 
  end = ''

  for i in range(len(words)):
    # 끝말잇기 시작이라면 word에 단어 추가하고, end 갱신 
    if not word :
      end = words[i][-1]
      word.add(words[i])
    else :
      # 등장한 단어거나 끝 문자와 시작 문자가 같지 않으면 
      if words[i] in word or words[i][0] != end:
        # 사람의 번호 
        num = (i+1) % n 
        if num == 0 :
          answer.append(n) 
        else:
          answer.append(num)
        # 차례 
        case = i // n  + 1
        answer.append(case)
        return answer
     # 등장하지 않은 단어이고 끝 문자와 시작 문자가 같다면 word에 추가 후 end 갱신 
      else :
        word.add(words[i])
        end = words[i][-1]
  
  return [0,0]