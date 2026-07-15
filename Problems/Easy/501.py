# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def findMode(self, root) -> list[int]:
        seen = {}
        def dfs(node):
            if node is None:
                return

            seen[node.val] = seen.get(node.val, 0) + 1

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_occurrence = max(seen.values())
        result = []
        for value in seen:
            if seen[value] == max_occurrence:
                result.append(value)
        return result
    
   
my_solution = Solution()
print(my_solution.findMode(root = [1,null,2,2]))   #Output: 2       
            
