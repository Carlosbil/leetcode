
# Intuition
"""
This problem requires reconstructing an array from a given set of adjacent pairs. It is akin to rebuilding
a path from a collection of its constituent segments. The key lies in understanding that the original 
array can be represented as a linear graph, where each node (except for the two end nodes) will have exactly 
two neighbors. The nodes at the ends of the array will have only one neighbor each. The problem, therefore, 
transforms into finding a path through this graph, starting from one of the end nodes and traversing through 
all nodes exactly once.
# Approach
To solve this problem, the algorithm employs the following steps:

1. Construct an Adjacency List: Convert the given adjacent pairs into an adjacency list. This list represents 
the graph where the indices are nodes, and the list values are neighboring nodes.

2. Identify the Start Node: Find a node that has only one neighbor. This node represents an end of the array 
(either start or end, as the array can be reconstructed in either direction).

3. Depth-First Search (DFS): Using a stack for DFS, start from the identified end node and traverse the graph. 
Keep track of visited nodes to avoid revisiting and to ensure we are not stuck in a cycle.

4. Reconstruct the Array: During the traversal, add each visited node to the result list. This sequential 
addition reconstructs the original array.


# Complexity
- Time complexity:
O(n)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

"""
from typing import List
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Create a dictionary to store the adjacency list
        adj_list = {}
        for pair in adjacentPairs:
            adj_list.setdefault(pair[0], []).append(pair[1])
            adj_list.setdefault(pair[1], []).append(pair[0])
        
        # Find the start of the array (a node with only one neighbor)
        start = None
        for node, neighbors in adj_list.items():
            if len(neighbors) == 1:
                start = node
                break
        
        # Traverse the array using the adjacency list
        result = []
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            result.append(node)
            for neighbor in adj_list[node]:
                stack.append(neighbor)
        
        return result
