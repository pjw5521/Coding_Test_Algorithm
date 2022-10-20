class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next # 다음 데이터 주소 초기값 : None
      
def add(data):
    node = head 
    
    while node.next:
        node = node.next 
    node.next= Node(data) 
     
# 노드 연결   
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1 

# node뒤에 값 추가 
node1 = Node(1)
head = node1
add(3)
