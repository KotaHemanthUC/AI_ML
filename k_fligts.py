from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create the adjacency list
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        # Initialize the stops array
        stops = [float('inf')] * n
        
        # Initialize the priority queue
        pq = [(0, src, 0)]
        
        while pq:
            dist, node, steps = heapq.heappop(pq)
            
            # If we've already encountered a path with a lower cost and fewer stops,
            # or the number of stops exceeds the limit, skip this path
            if steps > stops[node] or steps > k + 1:
                continue
            
            stops[node] = steps
            
            if node == dst:
                return dist
            
            for neighbor, price in adj[node]:
                heapq.heappush(pq, (dist + price, neighbor, steps + 1))
        
        return -1
