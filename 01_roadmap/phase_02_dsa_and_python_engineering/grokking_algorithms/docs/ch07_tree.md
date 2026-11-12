# Chapter 7 — Trees

> *Grokking Algorithms, 2nd Edition — Aditya Bhargava*

## 1. Tree Terminology

A **tree** is a type of graph made of nodes and edges.

- **Root:** The starting node of a rooted tree.
- **Parent:** A node directly above another node.
- **Child:** A node directly below another node.
- **Leaf:** A node with no children.
- Each node has at most one parent.
- A rooted tree has one root, and every other node is a descendant of the root.

## 2. Breadth-First Search (BFS) on Trees

**Breadth-first search (BFS)** traverses a tree by exploring nodes level by level.

The book uses BFS to list all files inside a directory and its subdirectories.

Basic process:
1. Add the starting directory to a queue.
2. Remove a directory from the queue.
3. Examine its files and subdirectories.
4. Print file names.
5. Add subdirectories to the queue.
6. Continue until the queue is empty.

Trees have no cycles, and each node has only one parent. Therefore, a traversal does not revisit nodes in a tree, so a separate `searched` collection is unnecessary in this example.

**Important:** A symbolic link can introduce a cycle into a file directory, meaning the directory structure is no longer a tree.

## 3. Depth-First Search (DFS)

**Depth-first search (DFS)** traverses a tree by exploring a branch as deeply as possible before returning to explore another branch.

The book demonstrates DFS using **recursion**:

- Examine each file and folder.
- Print a file's name.
- If an entry is a folder, call the function recursively on that folder.

Unlike BFS, DFS does not need a queue in this example; the recursion uses the call stack instead.

### BFS vs. DFS

| | BFS | DFS |
|---|---|---|
| **Order** | Level by level | Deep along one branch, then backtrack |
| **Uses** | A queue | Recursion (the call stack) in the book's example |
| **Shortest path (unweighted graph)** | Can find it | Not generally guaranteed |

Both can traverse a tree and list its files.

DFS is also used for topological sorting.

## 4. A Better Definition of Trees

A tree is a **connected, acyclic graph**.

- **Connected:** There is a path between every pair of nodes.
- **Acyclic:** The graph contains no cycles.
- A **cycle** is a path that returns to its starting node.

The absence of cycles is a key property of trees.

## 5. Binary Trees

A **binary tree** is a tree in which each node can have at most two children:

- **Left child**
- **Right child**

A **left subtree** or **right subtree** is the subtree rooted at the corresponding child.

Binary trees are common in computer science. The chapter uses one to explain Huffman coding.

## 6. Bits, Bytes, and Character Encoding

- A **bit** is a binary digit: `0` or `1`.
- A **byte** contains 8 bits.
- A character encoding represents characters as binary data.

The chapter introduces these encodings and standards:

| Name | What it is | Details |
|---|---|---|
| **ASCII** | Encoding | 7 bits, 128 possible values |
| **ISO-8859-1** | Encoding | 8 bits, 256 possible values |
| **Unicode** | Character standard | Intended to provide characters for languages around the world |
| **UTF-8** | Unicode encoding | Variable length, 1–4 bytes per character in the chapter's explanation |

Unicode is the standard; UTF-8 is an encoding that follows it.

**Key takeaway:** UTF-8 is a good default choice for encoding text in a project.

## 7. Huffman Coding

**Huffman coding** is a technique used in text compression. It tries to reduce the number of bits needed to represent the characters in a piece of text.

With a fixed-length encoding such as the chapter's ISO-8859-1 example, each character uses 8 bits. Huffman coding can use variable-length codes instead.

### How It Works

- Characters that appear more frequently can receive shorter codes.
- Less frequent characters can receive longer codes.
- A binary tree represents the codes.
- Start at the root and follow the path to a character.
- Each move to the **left** adds `0` to the code.
- Each move to the **right** adds `1`.
- Stop when the character is reached.

Because frequent characters use fewer bits, the total data can be smaller, especially in longer texts.

### Decoding Huffman Codes

To decode a sequence of bits:

1. Start at the root.
2. Read one bit at a time.
3. Follow left for `0` and right for `1`.
4. When a character is reached, output it.
5. Return to the root and decode the remaining bits.

Huffman codes have variable lengths, so the data cannot be decoded by splitting it into equal-sized chunks.

### Why Trees Matter in Huffman Coding

The tree structure provides several important properties:

- **Leaf nodes contain characters:** A character's code ends at a leaf.
- **No ambiguous prefixes:** One character's code cannot be the beginning of another character's complete code.
- **A unique path:** Each leaf has one path from the root, giving its character one code.

These properties allow variable-length codes to be decoded without ambiguity.

## Key Takeaways

- Trees are connected, acyclic graphs.
- Rooted trees have a root, and nodes can have parents and children.
- BFS explores level by level using a queue.
- DFS explores deeply before backtracking; the chapter demonstrates it with recursion.
- BFS can find shortest paths in unweighted graphs; DFS cannot generally guarantee them.
- Binary trees have at most two children per node.
- A bit is `0` or `1`; a byte contains 8 bits.
- Unicode is a character standard, while UTF-8 is a common variable-length encoding for Unicode text.
- Huffman coding compresses data by assigning variable-length codes, with shorter codes for more frequent characters.
- Huffman coding uses a binary tree so codes can be decoded unambiguously.
