# Chapter 6 — Breadth-First Search

# ============================================================
# Stage 1: The Problem — Finding a Mango Seller
# ============================================================

# We own a mango farm and want to find someone who sells mangoes.
# We need to search through our network of friends.
# The closest seller is preferable to a seller many connections away.


# ============================================================
# Stage 2: Modeling Relationships with a Graph
# ============================================================

# A graph consists of nodes and edges.
# Nodes represent people.
# Edges represent relationships between people.
#
# A dictionary maps each person to their outgoing neighbors.

graph = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}

# An empty list means that a person has no outgoing neighbors.
# The person may still have incoming connections.


# ============================================================
# Stage 3: Directed Graphs
# ============================================================

# This is a directed graph.
# If "you" points to "alice", the relationship is one-way.
# It does not automatically mean "alice" points back to "you".

directed_graph = {
    "you": ["alice"],
    "alice": [],
}

# An undirected relationship works in both directions.
# In an adjacency-list representation, both connections
# would be stored explicitly.

undirected_graph = {
    "you": ["alice"],
    "alice": ["you"],
}


# ============================================================
# Stage 4: The Search Order Matters
# ============================================================

# First-degree connections are direct neighbors.
# Second-degree connections are neighbors of our neighbors.
#
# We should check first-degree connections before second-degree
# connections if we want the closest seller.

first_degree = graph["you"]

print("First-degree connections:", first_degree)

# Claire is a first-degree connection.
# Anuj is a second-degree connection through Bob.
# Therefore, Claire must be checked before Anuj.


# ============================================================
# Stage 5: A Queue — FIFO
# ============================================================

from collections import deque  # noqa

search_queue = deque()

# Add the starting person's neighbors to the queue.
search_queue.extend(graph["you"])

# FIFO means First In, First Out.
# The first person added is the first person removed.

print("Initial queue:", list(search_queue))

first_person = search_queue.popleft()

print("First person to search:", first_person)
print("Remaining queue:", list(search_queue))


# ============================================================
# Stage 6: Defining a Mango Seller
# ============================================================

# This is the book's simple example:
# a name ending in "m" represents a mango seller.
# It is only a demonstration, not a real business rule.


def person_is_seller(name):
    return name.endswith("m")


# ============================================================
# Stage 7: Breadth-First Search (BFS)
# ============================================================


def search_mango_seller(start):
    search_queue = deque()
    search_queue.extend(graph[start])

    # Keep track of people already searched.
    searched = set()

    while search_queue:
        person = search_queue.popleft()

        # Avoid searching the same person more than once.
        # Note: checking on dequeue (as shown here) is functionally
        # correct but may add duplicates to the queue.
        # Checking on enqueue (before adding to the queue) is more
        # efficient — it prevents duplicates from entering the queue.
        if person in searched:
            continue

        if person_is_seller(person):
            print(f"{person} is a mango seller!")
            return person

        # Search this person's neighbors next.
        search_queue.extend(graph[person])
        searched.add(person)

    # The queue is empty: no seller was found.
    print("No mango seller was found.")
    return None


seller = search_mango_seller("you")


# ============================================================
# Stage 8: Why We Need a Visited Set
# ============================================================

# Alice and Bob both connect to Peggy.
# Without tracking searched people, Peggy may be added
# to the queue more than once.

graph_with_shared_friend = {
    "you": ["alice", "bob"],
    "alice": ["peggy"],
    "bob": ["peggy"],
    "peggy": [],
}

# Cycles can also cause an endless search if visited people
# are never tracked.

cyclic_graph = {
    "you": ["peggy"],
    "peggy": ["you"],
}

# The searched set prevents re-processing nodes and infinite loops
# caused by cycles.
#
# Without it, a cyclic graph causes infinite traversal:
#
#     you → peggy → you → peggy → ...
#
# With it, each node is processed exactly once.


# ============================================================
# Stage 9: BFS and the Shortest Path
# ============================================================

# BFS explores the graph level by level:
#
# Level 0: the starting node
# Level 1: direct neighbors
# Level 2: neighbors of direct neighbors
# Level 3: the next level of connections
#
# In an unweighted graph, BFS finds the shortest path
# measured by the number of edges.
#
# This works because the queue preserves discovery order.
# A stack would explore in a different order and would not
# guarantee the shortest path.


# ============================================================
# Stage 10: BFS Can Answer Two Questions
# ============================================================

# Question 1:
# Is there a path from node A to node B?
#
# Question 2:
# What is the shortest path from node A to node B?
#
# Searching for any mango seller demonstrates the first question.
# Searching level by level for the closest seller demonstrates
# the second question.


# ============================================================
# Stage 11: BFS Running Time
# ============================================================

# V = number of vertices (nodes)
# E = number of edges (connections)
#
# BFS takes O(V + E) time when using an adjacency-list graph
# and a queue with efficient operations.
#
# Each vertex is processed at most once, and each edge
# is examined at most once during a full traversal.


# ============================================================
# Stage 12: Dependencies Between Tasks
# ============================================================

# A directed graph can represent task dependencies.
# An arrow from task A to task B means B depends on A.

dependencies = {
    "wake_up": ["shower", "brush_teeth"],
    "shower": [],
    "brush_teeth": ["eat_breakfast"],
    "eat_breakfast": [],
}

# One valid order is:
#
# 1. wake_up
# 2. shower
# 3. brush_teeth
# 4. eat_breakfast
#
# Another valid order is:
#
# 1. wake_up
# 2. brush_teeth
# 3. shower
# 4. eat_breakfast
#
# Showering and brushing teeth can switch order,
# but breakfast must come after brushing teeth.


# ============================================================
# Stage 13: Topological Sort
# ============================================================

# Topological sort produces an ordering of nodes that respects
# the dependencies in a directed graph.
#
# If task B depends on task A, A must appear before B.
#
# This is useful for planning projects, preparing a wedding,
# or ordering tasks that have prerequisites.
#
# This chapter introduces the concept and examples of valid
# orderings; the code above models the dependencies but does
# not implement a topological-sort algorithm.


# ============================================================
# Stage 14: Trees Are a Special Kind of Graph
# ============================================================

# A family tree can be modeled as a graph.
# In the book's example, edges point toward parents.
#
# A tree is a special kind of graph.
# The chapter introduces this idea before the next chapter
# explores trees in more detail.


# ============================================================
# Stage 15: Final Mental Model
# ============================================================

# Graph:
# Models relationships using nodes and edges.
#
# BFS:
# Searches a graph level by level.
#
# Queue:
# Preserves search order using FIFO.
#
# Visited set:
# Prevents repeatedly searching the same nodes.
#
# Shortest path:
# BFS finds the path with the fewest edges in an unweighted graph.
#
# Topological sort:
# Orders tasks while respecting dependencies.
