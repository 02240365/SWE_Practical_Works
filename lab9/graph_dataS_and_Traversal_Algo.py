# Step 1: Implement the Graph Class

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()




# Step 2: Implement Depth-First Search (DFS)

class Graph:
    def __init__(self):
        """Initialize an empty graph as a dictionary."""
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def dfs(self, start_vertex):
        """Perform DFS starting from the given vertex."""
        visited = set()  # Set to keep track of visited vertices
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        """Recursive helper function for DFS."""
        visited.add(vertex)
        print(vertex, end=' ')  # Print the current vertex
        
        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Test DFS
print("DFS starting from vertex 0:")
g.dfs(0)






# Step 3: Implement Breadth-First Search (BFS)

from collections import deque

class Graph:
    def __init__(self):
        """Initialize an empty graph as a dictionary."""
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def bfs(self, start_vertex):
        """Perform BFS starting from the given vertex."""
        visited = set()  # Set to keep track of visited vertices
        queue = deque([start_vertex])  # Initialize the queue with the starting vertex
        visited.add(start_vertex)  # Mark the starting vertex as visited

        while queue:
            vertex = queue.popleft()  # Dequeue a vertex
            print(vertex, end=' ')  # Print the current vertex

            # Enqueue all unvisited neighbors
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark as visited
                    queue.append(neighbor)  # Add to queue

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Test BFS
print("BFS starting from vertex 0:")
g.bfs(0)






# Step 4: Implement a Method to Find All Paths

class Graph:
    def __init__(self):
        """Initialize an empty graph as a dictionary."""
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def find_all_paths(self, start_vertex, end_vertex, path=None):
        """Find all paths from start_vertex to end_vertex."""
        if path is None:
            path = []  # Initialize path on first call
        path = path + [start_vertex]  # Add current vertex to path

        if start_vertex == end_vertex:  # If the current vertex is the end vertex
            return [path]  # Return the current path

        if start_vertex not in self.graph:  # If the start vertex is not in the graph
            return []  # No paths to return

        paths = []  # List to store all paths
        for neighbor in self.graph[start_vertex]:  # Explore neighbors
            if neighbor not in path:  # Avoid revisiting vertices
                new_paths = self.find_all_paths(neighbor, end_vertex, path)  # Recursive call
                for new_path in new_paths:  # Collect all new paths
                    paths.append(new_path)
        return paths  # Return all found paths

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Test finding all paths
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))




# Step 5: Implement a Method to Check if the Graph is Connected

class Graph:
    def __init__(self):
        """Initialize an empty graph as a dictionary."""
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []  # Initialize the vertex with an empty list

    def _dfs_recursive(self, vertex, visited):
        """Helper function for depth-first search."""
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def is_connected(self):
        """Check if the graph is connected."""
        if not self.graph:
            return True  # An empty graph is considered connected
        start_vertex = next(iter(self.graph))  # Get an arbitrary starting vertex
        visited = set()
        self._dfs_recursive(start_vertex, visited)  # Perform DFS from the starting vertex
        return len(visited) == len(self.graph)  # Check if all vertices were visited

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

# Test if the graph is connected
print("\nIs the graph connected?", g.is_connected())

# Add a disconnected vertex and test again
g.add_vertex(4)  # This vertex is already in the graph but is not connected
g.add_vertex(5)  # Adding a new disconnected vertex
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())






# Exercises


# 1.Find the Shortest Path Between Two Vertices Using BFS

def shortest_path(self, start_vertex, end_vertex):
    """Find the shortest path between two vertices using BFS."""
    visited = set()
    queue = deque([[start_vertex]])  # Initialize queue with the start vertex in a path

    while queue:
        path = queue.popleft()
        vertex = path[-1]  # Get the last vertex in the current path

        if vertex == end_vertex:
            return path  # Return the path if we reached the end vertex
        
        if vertex not in visited:
            visited.add(vertex)  # Mark the vertex as visited

            for neighbor in self.graph[vertex]:
                new_path = list(path)  # Create a new path
                new_path.append(neighbor)  # Append the neighbor to the path
                queue.append(new_path)  # Add new path to the queue
    return None  # Return None if no path exists

# Add to Graph class and test
Graph.shortest_path = shortest_path

# Test the shortest path method
print("\nShortest path from vertex 0 to vertex 3:")
shortest = g.shortest_path(0, 3)
print(' -> '.join(map(str, shortest))) if shortest else print("No path found")




# 2.Detect Cycles in the Graph

def has_cycle(self):
    """Detect cycles in the graph using DFS."""
    visited = set()

    def _has_cycle_recursive(vertex, parent):
        visited.add(vertex)  # Mark the vertex as visited
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if _has_cycle_recursive(neighbor, vertex):  # Recur for DFS
                    return True
            elif parent != neighbor:  # Check for back edges
                return True
        return False

    for vertex in self.graph:
        if vertex not in visited:
            if _has_cycle_recursive(vertex, None):
                return True  # Cycle detected
    return False  # No cycles detected

# Add to Graph class and test
Graph.has_cycle = has_cycle

# Test for cycles
print("\nDoes the graph have a cycle?", g.has_cycle())





# 3.Implement Dijkstra's Algorithm

import heapq

def dijkstra(self, start_vertex):
    """Find the shortest paths from start_vertex to all other vertices using Dijkstra's algorithm."""
    # Create a priority queue
    queue = []
    heapq.heappush(queue, (0, start_vertex))  # (distance, vertex)
    distances = {vertex: float('inf') for vertex in self.graph}  # Initialize distances
    distances[start_vertex] = 0  # Distance to start vertex is 0
    previous_vertices = {vertex: None for vertex in self.graph}  # Track previous vertices

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)  # Get vertex with the smallest distance

        for neighbor in self.graph[current_vertex]:
            distance = current_distance + 1  # Assuming all edges have a weight of 1
            if distance < distances[neighbor]:  # Relaxation
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_vertices  # Return the distances and the path information

# Add to Graph class and test
Graph.dijkstra = dijkstra

# Test Dijkstra's algorithm (Note: graph should be initialized with weights)
print("\nShortest paths from vertex 0:")
distances, previous = g.dijkstra(0)
print(distances)





# 4.Check if the Graph is Bipartite

def is_bipartite(self):
    """Check if the graph is bipartite."""
    color = {}
    
    def bfs(start_vertex):
        queue = deque([start_vertex])
        color[start_vertex] = 0  # Color the start vertex with color 0

        while queue:
            vertex = queue.popleft()
            for neighbor in self.graph[vertex]:
                if neighbor not in color:  # If the neighbor hasn't been colored
                    color[neighbor] = 1 - color[vertex]  # Assign alternate color
                    queue.append(neighbor)
                elif color[neighbor] == color[vertex]:  # If same color as parent
                    return False  # Not bipartite
        return True

    for vertex in self.graph:
        if vertex not in color:  # If the vertex hasn't been colored
            if not bfs(vertex):  # Check using BFS
                return False  # Not bipartite

    return True  # All vertices colored successfully

# Add to Graph class and test
Graph.is_bipartite = is_bipartite

# Test bipartite check
print("\nIs the graph bipartite?", g.is_bipartite())