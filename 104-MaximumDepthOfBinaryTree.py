# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = int(self.maxDepth(root.left))
        right = int(self.maxDepth(root.right))

        if left > right :
            return left + 1
        else:
            return right + 1
