#https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    command = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    answer = 0
    result = set()
    x, y = 0,0 
    
    for i in dirs :
      next_x, next_y = x + command[i][0], y + command[i][1]
      if ( -5 <= next_x <= 5 and -5 <= next_y <= 5 ):
        result.add((x,y,next_x, next_y))
        result.add((next_x,next_y,x, y))
        x, y= next_x, next_y
    
    return len(result)//2 