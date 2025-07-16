class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')  # Track the overall max path sum

        def dfs(node):
            if not node:
                return 0

            # Get max gain from left and right (ignore negatives by taking max with 0)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Max path through the current node (including both children)
            current_max = node.val + left_gain + right_gain

            # Update global max if this path is better
            self.maxSum = max(self.maxSum, current_max)

            # Return max gain that can be extended to parent
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.maxSum


