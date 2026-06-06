# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        vals_set = set()

        while node.next!= None:
            print("Current node value: ", node.val)
            if node.val in vals_set:
                return True
            else:
                vals_set.add(node.val)
                print("Current set: ", vals_set)
                node = node.next
        return False