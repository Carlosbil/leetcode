import heapq
from typing import List

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = {i: [] for i in range(n)}
        # extract edges
        for from_node, to_node, cost in edges:
            self.graph[from_node].append((to_node, cost))

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        # Use Dijkstra's algorithm
        # Initialize all node distances as infinity
        distances = {node: float('infinity') for node in self.graph}
        # Set the distance for the starting node to zero
        distances[node1] = 0
        # Create a priority queue and add the starting node with a priority of zero
        priority_queue = [(0, node1)]

        # Loop while the priority queue is not empty
        while priority_queue:
            # Pop the node with the smallest distance
            current_distance, current_node = heapq.heappop(priority_queue)
            # If the current node is the target node, return its distance
            if current_node == node2:
                return current_distance

            # If the current node's distance is greater than its recorded distance, skip it
            if current_distance > distances[current_node]:
                continue

            # Loop through the current node's neighbors
            for neighbor, weight in self.graph[current_node]:
                # Calculate the distance to the neighbor through the current node
                distance = current_distance + weight
                # If the calculated distance is less than the recorded distance, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    # Add the neighbor to the priority queue with the updated distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return -1 if distances[node2] == float('infinity') else distances[node2]