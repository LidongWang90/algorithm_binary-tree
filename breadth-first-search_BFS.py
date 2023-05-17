# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        counter = 0
        # make a queue
        q = collections.deque()
        q.append(root)
        if not root:
            return 0
        # pop out and append node/nodes in a single round
        while len(q):
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            counter += 1
        return counter


# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        counter = 0
        q = collections.deque()
        q.append(root)
        if not root:
            return 0
        while len(q) != 0:
            for i in range(len(q)):
                node = q.popleft()
                for i in node.children:
                    q.append(i)
            counter += 1
        return counter
