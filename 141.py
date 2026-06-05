# 141. Linked List Cycle
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head     
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    
my_solution = Solution()
print(my_solution.hasCycle([3,2,0,-4]))  # Output: True
print(my_solution.hasCycle([1,2]))  # Output: False
    
