# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0         # Counter to track how many nodes we've visited
        self.result = None     # Will store the kth smallest value

        def inorder(node):
            if not node or self.result is not None:
                return

            inorder(node.left)  # Traverse left subtree

            self.count += 1     # Visit current node
            if self.count == k:
                self.result = node.val
                return

            inorder(node.right) # Traverse right subtree

        inorder(root)
        return self.result
