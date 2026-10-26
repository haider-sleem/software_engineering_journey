"""
Grokking Data Structures — Chapter 13
Graphs: Learning How to Model Complex Relationships in Data

Story:
A community wants to model who knows whom. Each person is a vertex and each
relationship is an edge. We use an adjacency list, then explore the graph
with BFS and DFS.
"""

from collections import deque

# 1. Model the community as an undirected graph.
# Each dictionary key is a vertex; its list contains adjacent vertices.
community = {
    "Alice": ["Bob", "Cara"],
    "Bob": ["Alice", "Dina", "Evan"],
    "Cara": ["Alice", "Farah"],
    "Dina": ["Bob"],
    "Evan": ["Bob", "Farah"],
    "Farah": ["Cara", "Evan"],
    "Gina": [],
    # A second, separate group, not connected to the first.
    "Hana": ["Ivan"],
    "Ivan": ["Hana"],
}


def show_neighbors(graph, person):
    """Display the vertices directly connected to person."""
    if person not in graph:
        print(f"{person} is not in the community.")
        return
    print(f"{person}'s direct connections: {graph[person]}")


show_neighbors(community, "Bob")


# 2. Add an undirected edge (a friendship in both directions).
def add_friendship(graph, person_a, person_b):
    if person_a not in graph or person_b not in graph:
        raise ValueError("Both people must already exist in the graph.")

    if person_b not in graph[person_a]:
        graph[person_a].append(person_b)
    if person_a not in graph[person_b]:
        graph[person_b].append(person_a)


add_friendship(community, "Dina", "Gina")


# 3. Breadth-First Search (BFS): explore vertices in nondecreasing order
# of distance from the start. A queue is FIFO: first in, first out.
def bfs(graph, start):
    if start not in graph:
        raise ValueError(f"Unknown starting vertex: {start}")

    visited = {start}
    queue = deque([start])
    visit_order = []

    while queue:
        person = queue.popleft()
        visit_order.append(person)

        for neighbor in graph[person]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visit_order


print("BFS from Alice:", bfs(community, "Alice"))


# 4. Find a shortest path in an unweighted graph using BFS.
# predecessor remembers the vertex from which each vertex was first reached.
def shortest_path_bfs(graph, start, target):
    if start not in graph or target not in graph:
        raise ValueError("Both start and target must exist in the graph.")

    queue = deque([start])
    predecessor = {start: None}

    while queue:
        person = queue.popleft()
        if person == target:
            break

        for neighbor in graph[person]:
            if neighbor not in predecessor:
                predecessor[neighbor] = person
                queue.append(neighbor)

    if target not in predecessor:
        return None

    path = []
    current = target
    while current is not None:
        path.append(current)
        current = predecessor[current]

    path.reverse()
    return path


print("Shortest path Alice -> Farah:", shortest_path_bfs(community, "Alice", "Farah"))


# 5. Depth-First Search (DFS): go deep, then backtrack.
# This version uses recursion (the call stack). An explicit stack is the
# common alternative. An explicit stack avoids Python's recursion limit
# on very deep graphs.
def dfs(graph, start):
    if start not in graph:
        raise ValueError(f"Unknown starting vertex: {start}")

    visited = set()
    visit_order = []

    def visit(person):
        visited.add(person)
        visit_order.append(person)

        for neighbor in graph[person]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return visit_order


print("DFS from Alice:", dfs(community, "Alice"))


# 6. Cycle detection with DFS and three colors (directed graph).
# White: not yet explored. Gray: currently being explored.
# Black: fully explored.
# Reaching a gray vertex means we came back to a vertex that is still
# being explored, so the graph contains a cycle.
WHITE, GRAY, BLACK = "white", "gray", "black"


# Assumption: every neighbor is also a key in directed_graph.
# This function detects cycles in directed graphs.
def has_cycle(directed_graph):
    color = {vertex: WHITE for vertex in directed_graph}

    def visit(vertex):
        color[vertex] = GRAY
        for neighbor in directed_graph[vertex]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and visit(neighbor):
                return True
        color[vertex] = BLACK
        return False

    return any(color[vertex] == WHITE and visit(vertex) for vertex in directed_graph)


tasks_with_cycle = {"A": ["B"], "B": ["C"], "C": ["A"]}
tasks_without_cycle = {"A": ["B", "C"], "B": ["C"], "C": []}

print("Cycle in A->B->C->A?", has_cycle(tasks_with_cycle))
print("Cycle in A->B, A->C, B->C?", has_cycle(tasks_without_cycle))

# This simple version is meant for directed graphs. In an undirected graph,
# every edge also points back to the vertex we came from, so the edge to the
# parent must be ignored before a gray vertex can signal a cycle.


# 7. Find connected components in an undirected graph.
# Each component contains vertices connected by paths.
# This traversal uses an explicit stack (DFS-style).
def connected_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex in visited:
            continue

        component = []
        stack = [vertex]
        visited.add(vertex)

        while stack:
            person = stack.pop()
            component.append(person)

            for neighbor in graph[person]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        components.append(component)

    return components


print("Connected components:", connected_components(community))


# 8. Build an adjacency matrix.
# Edge lookup is O(1), but the matrix takes O(V^2) space.
def to_adjacency_matrix(graph):
    vertices = list(graph)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    matrix = [[0 for _ in vertices] for _ in vertices]

    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            matrix[index[vertex]][index[neighbor]] = 1

    return vertices, matrix


vertices, matrix = to_adjacency_matrix(community)
alice_index = vertices.index("Alice")
bob_index = vertices.index("Bob")
print("Matrix vertex order:", vertices)
print("Is Alice connected to Bob?", bool(matrix[alice_index][bob_index]))


# 9. A tree is a special graph: simple, undirected, connected, and acyclic.
# Our community graph contains a cycle:
# Alice -> Bob -> Evan -> Farah -> Cara -> Alice
# Therefore, it is not a tree. A forest is an acyclic undirected graph
# that may have multiple connected components.


# 10. Complexity and when to use each idea.
# With an adjacency list, BFS and DFS take O(V + E), where V is the number
# of vertices and E is the number of edges.
# BFS finds a path with the fewest edges in an unweighted graph.
# For weighted shortest paths, use an algorithm such as Dijkstra's.
