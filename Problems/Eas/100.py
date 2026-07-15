# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
my_solution = Solution()
print(my_solution.isSameTree([1, 2, 3], [1, 2, 3])) # True
print(my_solution.isSameTree([1, 2], [1, None, 2])) # False
print(my_solution.isSameTree([1, 2, 1], [1, 1, 2])) # False