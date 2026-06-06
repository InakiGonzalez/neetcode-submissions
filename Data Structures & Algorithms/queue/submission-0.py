class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newnode = ListNode(value)
        last_node = self.tail.prev
        last_node.next = newnode
        newnode.prev = last_node
        newnode.next = self.tail
        self.tail.prev = newnode
            


    def appendleft(self, value: int) -> None:
        newnode = ListNode(value)
        first_node = self.head.next
        newnode.next = first_node
        first_node.prev = newnode
        self.head.next = newnode
        newnode.prev = self.head

        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.val
        curr_lastnode = last_node.prev
        curr_lastnode.next = self.tail
        self.tail.prev = curr_lastnode
        return value 
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.val
        curr_firstnode = first_node.next
        self.head.next = curr_firstnode
        curr_firstnode.prev = self.head
        return value
        
