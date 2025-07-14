import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        # Step 2: Priority queue -> (cost so far, current city, stops used)
        heap = [(0, src, 0)]  # (cost, node, stops)

        # Step 3: Modified Dijkstra's with max stops allowed = k
        while heap:
            cost, node, stops = heapq.heappop(heap)

            # If destination is reached within allowed stops
            if node == dst:
                return cost

            # If we can still take more stops
            if stops <= k:
                for neighbor, price in graph[node]:
                    new_cost = cost + price
                    heapq.heappush(heap, (new_cost, neighbor, stops + 1))

        return -1  # No path found within K stops
