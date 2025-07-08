from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Step 1: Build the graph (adjacency list)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        # Step 2: DFS function
        def dfs(node, parent):
            if node in visited:
                return False  # cycle detected
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # skip the parent
                if not dfs(neighbor, node):
                    return False
            return True

        # Step 3: Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Step 4: Check if all nodes are connected
        return len(visited) == n
