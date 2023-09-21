# Time Complexity: O(n)
# Space Complexity: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        if root is None:
            return 0

        def helper(root, curr_sum):
            if root is None:
                return
            helper(root.left,curr_sum*10+root.val)
            if root.left is None and root.right is None:
                self.sum += curr_sum*10 + root.val
            helper(root.right,curr_sum*10+root.val)
        helper(root,0)
        return self.sum
