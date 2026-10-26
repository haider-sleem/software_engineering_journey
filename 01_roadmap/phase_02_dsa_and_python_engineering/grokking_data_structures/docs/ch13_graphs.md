# Chapter 13 — Graphs

> *Grokking Data Structures — Marcello La Rocca*

## 1. What Is a Graph?

A **graph** models relationships between entities.

A graph consists of:

- **Vertices (V):** The entities or objects.
- **Edges (E):** The connections between vertices.

A graph is represented as `G = (V, E)`.

Examples:
- Social networks: people and friendships.
- Maps: locations and roads.
- Computer networks: devices and connections.
- Workflows: tasks and dependencies.

## 2. Types of Graphs

- **Directed graph:** Edges have a direction. Example: one user follows another.
- **Undirected graph:** Edges can be traversed in both directions. Example: mutual friendship.
- **Weighted graph:** Edges have numerical values, such as distances or costs.
- **Loop:** An edge whose source and destination are the same vertex.
- **Simple graph:** Has no loops and at most one edge between any pair of vertices.
- **Multigraph:** Can have multiple edges between the same vertices.
- **Cyclic graph:** Contains a path that starts and ends at the same vertex.
- **Acyclic graph:** Contains no cycles.
- **Sparse graph:** Has relatively few edges compared with the maximum possible number of edges; often `O(V)` in common examples.
- **Dense graph:** Has many edges, potentially `O(n²)`.

## 3. Paths and Connectivity

- **Path:** A sequence of edges connecting vertices.
- **Cycle:** A path that starts and ends at the same vertex.
- **Subgraph:** A graph formed from a subset of another graph's vertices and edges.
- **Connected graph:** An undirected graph in which every pair of vertices has a path between them.
- **Connected components:** Maximal connected parts of a graph.
- **Strongly connected vertices:** In a directed graph, each vertex can reach the other.
- **Strongly connected component:** A maximal subgraph in which every vertex can reach every other vertex.
- **Weakly connected graph:** A directed graph that becomes connected when edge directions are ignored.

A **tree** is a simple, connected, undirected, acyclic graph. A tree with `n` vertices has exactly `n - 1` edges.

A **forest** is an undirected, acyclic graph that may contain multiple connected components.

## 4. Graph Representations

### Adjacency List

An **adjacency list** stores the outgoing neighbors of each vertex.

It can be implemented using a dictionary whose values are lists, sets, or other containers.

```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
```

- Efficient for traversing a vertex's neighbors.
- Usually more space-efficient for sparse graphs.
- Checking whether a specific edge exists requires searching the relevant adjacency list.

### Adjacency Matrix

An **adjacency matrix** uses a two-dimensional array to represent edges.

- Rows represent source vertices.
- Columns represent destination vertices.
- A cell indicates whether an edge exists or stores its weight.

Checking whether an edge exists takes `O(1)` time.

However, the matrix requires `O(V²)` space, even when the graph has few edges. It is most useful when the graph is dense or frequent edge-existence checks are required.

## 4b. Graph Implementation

The graph is typically implemented using a class that maps vertex IDs to `Vertex` objects. Each `Vertex` stores its own adjacency list of outgoing edges.

**Core operations** *(illustrative names — verify against the source code):*

- `add_vertex(id)` — creates a new `Vertex` and registers it.
- `add_edge(u, v)` — adds `v` to `u`'s adjacency list (and `u` to `v`'s for undirected graphs).

> **Implementation Note:** Deleting a vertex requires removing all incoming edges from other vertices, not just removing the vertex from the dictionary. Failing to do so leaves dangling references in other adjacency lists.

---

## 5. Breadth-First Search (BFS)

**BFS** explores a graph from a starting vertex by expanding the frontier of directly and indirectly connected vertices.

It explores vertices one by one, using a **queue (FIFO)** to ensure that closer vertices are explored before more distant ones.

Main steps:

1. Add the starting vertex to the queue.
2. Remove the front vertex.
3. Examine its outgoing edges.
4. Add each undiscovered neighbor to the queue.
5. Repeat until the target is found or the queue is empty.

When a vertex is first discovered, its distance from the start is the minimum number of edges needed to reach it.

BFS can find a shortest path measured by the **number of edges** in an unweighted graph.

The book tracks two values per vertex during BFS:

- **`distance`** — the minimum number of edges from the starting vertex.
- **`predecessor`** — the previous vertex on the shortest path.

To reconstruct the path, follow `predecessor` links from the target back to the source, then reverse the result.

- If the target is unreachable, no path exists.
- Add each vertex to the queue only once, when its minimum distance from the start is first determined.
- For weighted shortest paths, use an appropriate algorithm such as Dijkstra's algorithm instead.

**Time complexity:** `O(V + E)` with an adjacency-list representation.

## 6. Depth-First Search (DFS)

**DFS** explores one path as deeply as possible before backtracking to explore alternatives.

The book implements DFS using an **explicit stack (LIFO)**. Recursion is a common alternative that uses the call stack implicitly.

DFS can be used for:

- Exploring reachable vertices.
- Finding connected components.
- Detecting cycles with suitable traversal state.
- Checking whether a directed graph is acyclic.
- Supporting topological sorting of directed acyclic graphs (DAGs).

> The chapter focuses on cycle detection; the other items are applications mentioned for further exploration.

Unlike BFS, DFS does **not** generally find the shortest path.

In the book's cycle-detection approach, vertices use three colors:

- **White:** Not yet explored.
- **Gray:** Currently being explored.
- **Black:** Fully explored.

Encountering a gray vertex during the appropriate DFS traversal indicates a cycle.

**Time complexity:** `O(V + E)` with an adjacency-list representation.

## 7. Key Takeaways

- Graphs model general relationships; trees model hierarchical relationships.
- Vertices represent entities, and edges represent connections.
- Directed edges represent one-way relationships; undirected edges represent two-way relationships.
- Adjacency lists are generally suitable for sparse graphs; adjacency matrices provide constant-time edge checks at a higher memory cost.
- BFS uses a queue and finds shortest paths by edge count in unweighted graphs.
- DFS uses a stack or recursion to explore paths deeply and can help detect cycles.
- Both BFS and DFS run in `O(V + E)` time with adjacency lists, when processing the graph's vertices and edges.
