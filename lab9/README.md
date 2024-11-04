# Graph Data Structure and Traversal Algorithms

This practical contains a Python implementation of a Graph data structure, featuring various algorithms for traversing, searching, and analyzing graphs. The implementation is versatile, allowing for the creation of undirected graphs and supporting various graph operations.

## Features

- **Graph Representation**: Uses an adjacency list to represent the graph.
- **Adding Vertices and Edges**: Methods to add vertices and edges to the graph.
- **Graph Traversal**:
  - **Depth-First Search (DFS)**: Explore all vertices in depth-first order.
  - **Breadth-First Search (BFS)**: Explore all vertices in breadth-first order.
- **Path Finding**:
  - Find all paths between two vertices.
  - Find the shortest path using BFS.
- **Connectivity Check**: Determine if the graph is connected.
- **Cycle Detection**: Check for cycles in the graph using DFS.
- **Dijkstra's Algorithm**: Calculate the shortest paths from a starting vertex to all other vertices.
- **Bipartite Check**: Verify if the graph can be colored using two colors without adjacent vertices sharing the same color.


## Example Usage

Here's an example of how to use the `Graph` class:

```python
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

# Print the graph
g.print_graph()

# Perform DFS
print("DFS starting from vertex 0:")
g.dfs(0)

# Perform BFS
print("\nBFS starting from vertex 0:")
g.bfs(0)

# Find all paths from vertex 0 to vertex 3
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))

# Check if the graph is connected
print("\nIs the graph connected?", g.is_connected())

# Shortest path from vertex 0 to vertex 3
print("\nShortest path from vertex 0 to vertex 3:")
shortest = g.shortest_path(0, 3)
print(' -> '.join(map(str, shortest))) if shortest else print("No path found")

# Cycle detection
print("\nDoes the graph have a cycle?", g.has_cycle())

# Dijkstra's algorithm
print("\nShortest paths from vertex 0:")
distances, previous = g.dijkstra(0)
print(distances)

# Bipartite check
print("\nIs the graph bipartite?", g.is_bipartite())
