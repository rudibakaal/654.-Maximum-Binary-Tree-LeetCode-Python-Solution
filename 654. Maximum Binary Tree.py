# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
            if not nums:
                return
            e = list(enumerate(nums))
            damax = max(e, key=lambda x: x[1])
            root = TreeNode(damax[1])

            root.left = self.constructMaximumBinaryTree(nums[:damax[0]])
            root.right = self.constructMaximumBinaryTree(nums[damax[0] + 1:])

            return root
