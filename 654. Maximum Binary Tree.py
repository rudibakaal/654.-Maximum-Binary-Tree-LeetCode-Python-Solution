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