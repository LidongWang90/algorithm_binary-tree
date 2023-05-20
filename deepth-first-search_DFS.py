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


# Consider all the leaves of a binary tree,
# from left to right order, the values of those leaves form a leaf value sequence.
# 给一个树，返回所有的叶子（从左到右）。先用DFS recursion的办法，再用BFS+stack的办法。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS办法：
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # use DFS
        arr1, arr2 = [], []

        def dfs(node, arr):
            if not node:
                return None
            elif not node.left and not node.right:
                arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)
            return arr

        if dfs(root1, arr1) == dfs(root2, arr2):
            return True
        return False


# BFS 办法：
# use BFS + stack:
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return []

        def bfs(root):
            arr = []
            stack = [root]
            while len(stack) != 0:
                node = stack.pop()
                if not node.left and not node.right:
                    arr.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return arr

        if bfs(root1) == bfs(root2):
            return True
        return False
