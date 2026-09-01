# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical = []
        previous = head
        current = head.next
        index = 1

        while current.next:
            if (current.val > previous.val and current.val > current.next.val):
                critical.append(index)
            elif (current.val < previous.val and current.val < current.next.val):
                critical.append(index)
            previous = current
            current = current.next
            index += 1

        if len(critical) < 2:
            return [-1, -1]
        min_distance = float("inf")

        for i in range(1, len(critical)):
            distance = critical[i] - critical[i - 1]
            if distance < min_distance:
                min_distance = distance
        max_distance = critical[-1] - critical[0]
        return [min_distance, max_distance]


my_solution = Solution()
print(my_solution.nodesBetweenCriticalPoints(head = [3,1]))   #Output: [-1, -1]
print(my_solution.nodesBetweenCriticalPoints(head = [5,3,1,2,5,1,2]))   #Output: [1, 3]
print(my_solution.nodesBetweenCriticalPoints(head = [1,3,2,2,3,2,2,2,7]))   #Output: [3, 3]