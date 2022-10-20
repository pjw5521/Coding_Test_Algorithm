# 10번동안 1~10까지 랜덤한 숫자를 출력하여 중복된 숫자가 있을 경우 true, false
import random

num = set()
for _ in range(10):
    n = random.randrange(1,11)
    
    if n in num :
        print('true')
    else :
        num.add(n)
        print('false')