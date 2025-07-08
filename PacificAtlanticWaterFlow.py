from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r, c, visited, prevHeight):
            # Check boundaries
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                heights[r][c] < prevHeight
            ):
                return
            # Mark this cell as visited for this ocean
            visited.add((r, c))

            # Explore neighbors (up, down, left, right)
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Start DFS from Pacific ocean edges (top row and left column)
        for c in range(cols):
            dfs(0, c, pacific_visited, float('-inf'))
        for r in range(rows):
            dfs(r, 0, pacific_visited, float('-inf'))

        # Start DFS from Atlantic ocean edges (bottom row and right column)
        for c in range(cols):
            dfs(rows - 1, c, atlantic_visited, float('-inf'))
        for r in range(rows):
            dfs(r, cols - 1, atlantic_visited, float('-inf'))

        # Intersection of cells reachable by both oceans
        result = list(pacific_visited & atlantic_visited)
        return result
