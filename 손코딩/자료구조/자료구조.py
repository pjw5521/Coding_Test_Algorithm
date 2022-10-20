from collections import deque 
import queue

# 배열 
array = [1,2,3,4,5]

# 큐 (FIFO)
q = queue.Queue()
q.put(1)
q.get()

# FILO
q = queue.LifoQueue()
q.put(1)
q.get()

# 우선순위 큐 
q = queue.PriorityQueue()
q.put((10,1))
q.put((11,2))
q.get() # (11,2) 출력 

# 스택 -> 리스트로 구현 
list = []
list.append(1)
list.pop()
