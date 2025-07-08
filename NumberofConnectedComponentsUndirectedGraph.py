class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        total = 0 
        visited = set()

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        for i in range(n):
            if i not in visited:
            dfs(i)
            total += 1

        return total
