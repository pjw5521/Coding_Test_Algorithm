class Node:
    def __init__(self, val = 0 , next= None):
        self.val = val
        self.next = next 
    
    def print_all(self):
        while self :
            print(self.val, end = " ")
            self = self.next 
        print()
        
class Solution:
    def reverse(self, current : Node, prev : Node) -> Node :
        if not current :
            return prev 
        next = current.next 
        current.next = prev 
        return self.reverse(next, current)    
    
    def reverseList(self, head:Node)->Node:
        return self.reverse(head,None)
        
solution = Solution()

l1 = Node(1)
l2 = Node(3, l1)
l3 = Node(5, l2)

print("Before :", end = " ")
l3.print_all()
result = solution.reverseList(l3)
print("After : ", end = " ")
result.print_all()