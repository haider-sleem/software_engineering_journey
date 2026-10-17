# Chapter 6 — Breadth-First Search

> *Grokking Algorithms — Aditya Bhargava*

---

## Graphs

- A **graph** consists of nodes (vertices) and edges that connect them.
- Graphs model relationships and networks: people, roads, connections.
- A **directed graph** has one-way connections.
- An **undirected graph** has two-way connections.
- A node's **neighbors** are the nodes directly connected to it.

---

## Breadth-First Search (BFS)

- BFS finds the shortest path in an **unweighted graph**, measured by the number of edges.
- It searches neighbors first, then neighbors of those neighbors — level by level.
- It can also answer reachability questions: does a path exist to the target at all?

---

## Implementing a Graph in Python

A hash table maps each node to a list of its outgoing neighbors:

```python
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}
```

- Keys represent nodes; values represent lists of outgoing neighbors.
- An empty list means the node has no outgoing neighbors.
- In a directed graph, A → B does not automatically imply B → A.

---

## Queues and BFS

| Structure | Order | Used in |
|-----------|-------|---------|
| **Queue** | FIFO — first in, first out | BFS |
| **Stack** | LIFO — last in, first out | DFS |

Nodes discovered earlier are processed earlier — this preserves the level-by-level order that makes BFS find the shortest path first.

---

## The BFS Process

1. Add the starting node's neighbors to the queue.
2. Remove the first node from the queue.
3. Check whether it matches the target.
4. If not, add its **unvisited** neighbors to the queue.
5. Repeat until the target is found or the queue is empty.

**Key rules:**
- Use a **`searched` set** to avoid searching the same person more than once.
- Check whether a person has already been searched **before processing them**.
- For each person not already in `searched`, process them and add them to `searched` if the search continues — following the book's implementation. If the target is found, the function returns immediately before adding them.

> **Alternative approach:** marking nodes as visited on enqueue (before adding to the queue) prevents duplicate entries in the queue. This is a common optimization and is not incorrect — it differs from the book's implementation but produces the same result.

- An empty queue with no match means no path exists.

---

## Finding the Shortest Path

- BFS explores paths in increasing order of edge count, so the first time a target is reached it is via the shortest path.

> **Implementation Extension (beyond the chapter):** to recover the actual path, store each discovered node's predecessor and trace back after reaching the target. The book focuses on finding the closest match, not on reconstructing the full path.

---

## Time and Space Complexity

| Resource | Complexity | Why |
|----------|-----------|-----|
| **Time** | O(V + E) | V = vertices visited, E = edges traversed |
| **Space** | O(V) | Queue and visited set both grow with the number of vertices *(analytical addition — not stated explicitly in this chapter)* |

---

## Common Applications

- Shortest route by number of connections.
- Finding the closest matching person or item in a network.
- Web crawling.
- Finding the minimum number of edits needed to turn a misspelled word into a valid word.

---

## Key Takeaways

- Graphs represent relationships between nodes.
- BFS explores a graph level by level using a FIFO queue.
- BFS finds shortest paths in **unweighted** graphs — not necessarily in weighted graphs.
- A visited set prevents repeated processing and infinite loops in cyclic graphs.
- The book marks a person as searched after processing them; marking nodes visited on enqueue is a common alternative.
