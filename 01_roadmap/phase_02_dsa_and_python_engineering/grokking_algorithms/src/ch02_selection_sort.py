def find_smallest(arr: list[int]) -> int:
    """Finds the index of the smallest element in a list.

    Args:
        arr (list[int]): A list of elements to search through.

    Returns:
        int: The index of the smallest element in the list.
    """
    # Assume the first element is the smallest
    smallest = arr[0]
    smallest_index = 0

    # Loop through the array starting from the second element
    for i in range(1, len(arr)):
        # Update smallest and its index if a smaller element is found
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr: list[int]) -> list[int]:
    """Sorts an array from smallest to largest using Selection Sort.

    Args:
        arr (list[int]): The original unsorted list.

    Returns:
        list[int]: A new list with elements sorted in ascending order.
    """
    new_arr = []
    # Create a copy to avoid modifying the original list
    copied_arr = arr.copy()

    # Repeat until the copied list is empty
    for i in range(len(copied_arr)):
        # Find the index of the smallest element in the remaining list
        smallest = find_smallest(copied_arr)
        # Remove the smallest element and add it to the new array
        new_arr.append(copied_arr.pop(smallest))

    return new_arr


# Test the selection_sort function and print the result
print(selection_sort([5, 3, 6, 2, 10]))
