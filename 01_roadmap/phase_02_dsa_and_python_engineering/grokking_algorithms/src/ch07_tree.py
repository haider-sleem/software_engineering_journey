"""
Grokking Algorithms — Chapter 7: Trees
A code story: exploring folders and compressing text
"""

from collections import deque

# ============================================================
# Story 1 — A File System Is a Tree
# ============================================================

# Imagine that we have a folder named "pics".
# It contains files and another folder named "2001".
#
# Tree terminology:
# - Root: the starting folder.
# - Parent: a folder containing another folder.
# - Child: a file or folder inside a parent.
# - Leaf: a node with no children.
#
# A tree is a connected, acyclic graph.
# Each node has at most one parent.


# This dictionary simulates a file system to show the shape of a tree.
# It is not a real file system: a real program would read folder
# contents from the disk, for example with os.listdir().
file_system = {
    "pics": ["a.png", "2001", "odyssey.png"],
    "2001": ["space.png"],
}


# ============================================================
# Story 2 — BFS: Explore Level by Level
# ============================================================


# Here BFS is used only to traverse the tree and list its files.
# It is not computing a shortest path, as it did in Chapter 6.
def list_files_bfs(start_folder, file_system):
    # BFS uses a queue to track folders waiting to be explored.
    queue = deque([start_folder])
    files = []

    while queue:
        current_folder = queue.popleft()

        for item in file_system[current_folder]:
            if item in file_system:
                # It is a folder, so explore it later.
                queue.append(item)
            else:
                # It is a file, so record its name.
                files.append(item)

    return files


print("BFS:", list_files_bfs("pics", file_system))

# BFS explores the current folder's entries before
# exploring the contents of its child folders.
#
# Output:
# BFS: ['a.png', 'odyssey.png', 'space.png']


# ============================================================
# Story 3 — DFS: Explore Deep Before Returning
# ============================================================


def list_files_dfs(folder, file_system):
    files = []

    for item in file_system[folder]:
        if item in file_system:
            # Enter the child folder immediately.
            files.extend(list_files_dfs(item, file_system))
        else:
            files.append(item)

    return files


print("DFS:", list_files_dfs("pics", file_system))

# DFS explores a child folder immediately before
# continuing with the remaining entries.
# The recursion uses the call stack instead of a queue.
#
# Output:
# DFS: ['a.png', 'space.png', 'odyssey.png']


# BFS and DFS can both traverse a tree.
# However, BFS can find the shortest path in an unweighted
# graph, while DFS cannot generally guarantee it.
#
# DFS is also used for topological sorting.
#
# Trees have no cycles, so this example does not need
# a separate visited set.
#
# A symbolic link can introduce a cycle into a file system,
# so real file-system traversal may need extra safeguards.


# ============================================================
# Story 4 — A Binary Tree
# ============================================================

# Now imagine that each node can have at most two children.
# This is a binary tree.
#
# Left branch  -> 0
# Right branch -> 1
#
# Huffman coding uses a binary tree to represent characters.

# This tree is built by hand to demonstrate encoding and decoding.
# It is not an implementation of the algorithm that builds a
# Huffman tree from character frequencies.
huffman_tree = {
    "left": {
        "left": "i",
        "right": "l",
    },
    "right": "t",
}


# ============================================================
# Story 5 — Follow a Path to Encode a Character
# ============================================================


def encode_character(character, tree, path=""):
    # A leaf contains a character rather than child branches.
    if isinstance(tree, str):
        if tree == character:
            return path
        return None

    # Search the left branch: append 0.
    left_result = encode_character(character, tree["left"], path + "0")
    if left_result is not None:
        return left_result

    # Search the right branch: append 1.
    return encode_character(character, tree["right"], path + "1")


print("Code for i:", encode_character("i", huffman_tree))
print("Code for l:", encode_character("l", huffman_tree))
print("Code for t:", encode_character("t", huffman_tree))

# Output:
# Code for i: 00
# Code for l: 01
# Code for t: 1


# ============================================================
# Story 6 — Decode the Bits
# ============================================================


def decode_bits(bits, tree):
    decoded_text = []
    current_node = tree

    for bit in bits:
        # Follow the branch selected by the current bit.
        if bit == "0":
            current_node = current_node["left"]
        elif bit == "1":
            current_node = current_node["right"]
        else:
            raise ValueError("Bits must contain only 0 and 1.")

        # A leaf means one character has been decoded.
        if isinstance(current_node, str):
            decoded_text.append(current_node)

            # Start again from the root for the next character.
            current_node = tree

    # If we stopped in the middle of a code, the input is incomplete.
    if current_node is not tree:
        raise ValueError("Incomplete Huffman code.")

    return "".join(decoded_text)


encoded_text = "00011"  # i (00) + l (01) + t (1)
print("Decoded text:", decode_bits(encoded_text, huffman_tree))

# Output:
# Decoded text: ilt


# ============================================================
# Story 7 — Why Huffman Coding Can Compress Text
# ============================================================

# Fixed-length encoding:
# Every character uses the same number of bits.
#
# Huffman coding:
# Characters can have different code lengths.
# More frequent characters can receive shorter codes.
#
# Example from our small tree:
#
# i -> 00   (2 bits)
# l -> 01   (2 bits)
# t -> 1    (1 bit)
#
# The encoded text "tilt" becomes:
#
# t + i  + l  + t
# 1 + 00 + 01 + 1 = 100011
#
# This example demonstrates variable-length codes.
# It is a simplified, manually constructed tree, not a
# complete implementation of the Huffman algorithm.
#
# Huffman coding is useful because frequent characters
# can use fewer bits, reducing the total data size.


# ============================================================
# Story 8 — Why the Tree Must Be Structured Correctly
# ============================================================

# Huffman characters are stored at leaf nodes.
#
# This prevents one character's code from being the prefix
# of another character's complete code.
#
# If a character appeared before a leaf, decoding could
# become ambiguous. For example:
#
# a -> 0
# b -> 1
# c -> 00
#
# The bits "001" could be interpreted in different ways.
#
# In a properly constructed Huffman tree:
# - Characters are stored at leaf nodes.
# - Each character has one path from the root.
# - No character's code is a prefix of another character's
#   complete code.


# ============================================================
# Story 9 — Character Encoding Is Different from Compression
# ============================================================

# A bit is 0 or 1.
# A byte contains 8 bits.
#
# Character encodings represent text as bytes:
#
# ASCII:
# A 7-bit encoding.
#
# ISO-8859-1:
# An 8-bit encoding used in the book's examples.
#
# Unicode:
# A standard for representing characters across languages.
#
# UTF-8:
# A variable-length encoding for Unicode text.
# Characters use between 1 and 4 bytes in UTF-8.
#
# Character encoding answers:
# "How is this character represented as bytes?"
#
# Huffman coding answers:
# "Can this text be represented using fewer bits?"
#
# UTF-8 is a good default choice for text encoding.


# ============================================================
# Chapter 7 — Final Mental Model
# ============================================================

# Tree:
# A connected graph without cycles.
#
# BFS:
# Explore level by level using a queue.
#
# DFS:
# Explore deeply before backtracking; recursion is one option.
#
# Binary tree:
# Each node has at most two children.
#
# Huffman coding:
# Use a binary tree to represent characters with
# variable-length binary codes.
#
# Main lesson:
# The structure of a tree can make traversal, searching,
# and unambiguous decoding possible.
