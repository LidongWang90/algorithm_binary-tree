# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# 中根：左——根——右的顺序：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
            return arr

        return dfs(root)
