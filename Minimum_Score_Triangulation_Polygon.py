class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        # dp[i][j] = minimum triangulation score for polygon vertices from i to j
        dp = [[0] * n for _ in range(n)]
        
        # length is the number of vertices in the current sub-polygon (starting from 3)
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                # Try all possible k to split the polygon (i, k, j)
                for k in range(i + 1, j):
                    cost = values[i] * values[k] * values[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[0][n-1]
