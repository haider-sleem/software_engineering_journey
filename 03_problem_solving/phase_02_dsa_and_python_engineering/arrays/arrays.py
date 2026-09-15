# 1 Source: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150


def has_duplicate(nums: list[int]) -> bool:
    """Determines if any value appears more than once in an array.

    This function leverages a hash set to efficiently detect duplicate
    elements by comparing the original list size against the unique
    elements set size.

    Args:
        nums (list[int]): The input list of integers to check.

    Returns:
        bool: True if any value appears more than once, False otherwise.
    """
    # Convert the list to a set. Sets only store unique elements,
    # which automatically removes any duplicates (O(n) time complexity).
    set_nums = set(nums)

    # If the original list is larger than the set, it means
    # duplicates existed and were filtered out by the set.
    return len(nums) > len(set_nums)


# 2 Source: https://neetcode.io/problems/is-anagram/question?list=neetcode150


def is_anagram(s: str, t: str) -> bool:
    """Determines if two strings are anagrams of each other using sorting.

    Args:
        s (str): The first input string.
        t (str): The second input string.

    Returns:
        bool: True if 's' and 't' are anagrams, False otherwise.

    Complexity:
        Time: O(n log n) due to sorting both strings, where n is the length.
        Space: O(n) to store the sorted character sequences.
    """
    return sorted(s) == sorted(t)


# 3 Source: https://neetcode.io/problems/two-integer-sum/question?list=neetcode150


def two_sum(arr: list[int], target: int) -> list[int]:
    """Finds the indices of two numbers in an array that add up to a target value.

    Args:
        arr (list[int]): The list of integers to search through.
        target (int): The target sum we want to achieve.

    Returns:
        list[int]: A list containing the two indices whose values add up
        to the target, with the smaller index positioned first.
    """
    # Dictionary to store numbers we've seen so far as keys and their indices as values
    seen_dict = {}

    for i, n in enumerate(arr):
        # Calculate the required complement to reach the target sum
        needed_n = target - n

        # Check if we have already encountered the complement number in previous iterations
        if needed_n in seen_dict:
            # Return the smaller index first (from the dictionary) followed by the current index
            return [seen_dict[needed_n], i]

        # Store the current number and its index for future lookups
        seen_dict[n] = i
