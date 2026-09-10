# 1- Source: https://neetcode.io/problems/binary-search/question?list=neetcode150


def search(nums: list[int], target: int) -> int:
    """
    Searches for a target integer in a sorted array using Binary Search.

    Args:
        nums: A list of integers sorted in ascending order.
        target: The integer value to search for.

    Returns:
        The index of target if found in nums, otherwise -1.

    Complexity:
        Time: O(log n)
        Space: O(1)
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        current_val = nums[mid]

        if current_val == target:
            return mid
        elif current_val > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# 2 Source: https://neetcode.io/problems/search-2d-matrix/question?list=neetcode150


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """
    Searches for a target integer in an m x n matrix using 2D Binary Search.

    Treats the 2D matrix as a virtual 1D sorted array by mapping 1D indices
    to 2D row and column positions.

    Args:
        matrix: A 2D list of integers where each row is sorted.
        target: The integer value to search for.

    Returns:
        True if target exists within the matrix, False otherwise.

    Complexity:
        Time: O(log(m * n))
        Space: O(1)
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    left_index = 0
    right_index = (num_rows * num_cols) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        # Map the 1D index back to 2D matrix row and column
        current_row = mid_index // num_cols
        current_col = mid_index % num_cols
        current_value = matrix[current_row][current_col]

        if current_value == target:
            return True

        if current_value > target:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1

    return False


# 3 Source: https://neetcode.io/problems/eating-bananas/question?list=neetcode150


def minEatingSpeed(piles: list[int], h: int) -> int:
    """
    Finds the minimum integer eating speed k to finish all bananas within h hours.

    Args:
        piles: A list of integers where each element is the number of bananas in a pile.
        h: The maximum number of hours available to eat all bananas.

    Returns:
        The minimum integer rate k (bananas per hour).

    Complexity:
        Time: O(n log m), where n is len(piles) and m is max(piles).
        Space: O(1), using only scalar variables.
    """
    low = 1
    high = max(piles)
    result = high

    while low <= high:
        # Test candidate speed k (middle point)
        k = (low + high) // 2

        consumed_hours = 0
        for pile in piles:
            # Formula to round up integer division: ceil(pile / k)
            consumed_hours += (pile + k - 1) // k

        if consumed_hours <= h:
            # Save k as a valid solution candidate
            result = k
            # Try to find a smaller valid speed on the left side
            high = k - 1
        else:
            low = k + 1

    return result


# 4 Source: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/history?list=neetcode150&submissionIndex=0


def findMin(nums: list[int]) -> int:
    """Finds the minimum element in a rotated sorted array using binary search.

    Args:
        nums: A list of unique integers rotated between 1 and n times.

    Returns:
        The minimum integer in the array.

    Complexity:
        Time: O(log n), where n is the length of nums.
        Space: O(1), using constant extra memory.
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If mid is greater than right, minimum is in the right unsorted part
        if nums[mid] > nums[right]:
            left = mid + 1
        # Otherwise, minimum is in the left part or at mid itself
        else:
            right = mid

    # Loop ends when left == right, pointing directly to the smallest element
    return nums[left]


# 5 Source:https://neetcode.io/problems/find-target-in-rotated-sorted-array/question?list=neetcode150


def search(nums: list[int], target: int) -> int:  # noqa: F811
    """Searches for a target value in a rotated sorted array using binary search.

    Args:
        nums: A list of unique integers sorted in ascending order and rotated
            between 1 and n times.
        target: The integer value to search for within the array.

    Returns:
        The zero-based index of target if found in nums; otherwise -1.

    Complexity:
        Time: O(log n), where n is the length of nums, as the search space
            is halved in each iteration.
        Space: O(1), as the search is performed in-place using constant extra
            memory.
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Found target
        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Check if target lies within the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, right half must be sorted
        else:
            # Check if target lies within the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# 6 Source: https://neetcode.io/problems/time-based-key-value-store/question?list=neetcode150


class TimeMap:
    """A time-based key-value data structure that stores multiple values

    for the same key at different timestamps.
    """

    def __init__(self):
        """Initializes the TimeMap object with an empty storage dictionary."""
        # Maps key (str) to a list of [timestamp, value] pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Stores the key with the value at the given timestamp.

        Args:
            key: The string key identifier.
            value: The string value to associated with the key.
            timestamp: The integer timestamp for the entry.
        """
        if key not in self.store:
            self.store[key] = []

        # Timestamps are strictly increasing, so the list remains sorted
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        """Retrieves the value associated with key at or before given timestamp.

        Args:
            key: The string key identifier to look up.
            timestamp: The target timestamp integer.

        Returns:
            The value string with the largest timestamp <= target timestamp.
            Returns an empty string if no such value exists.
        """
        values = self.store.get(key, [])
        res = ""

        # Binary search pointers based on array indices
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            # Exact timestamp match found
            if values[mid][0] == timestamp:
                return values[mid][1]

            # Current timestamp is valid; save candidate and search right for a closer one
            elif values[mid][0] < timestamp:
                res = values[mid][1]
                left = mid + 1

            # Current timestamp is too large; search left
            else:
                right = mid - 1

        return res


# 7 Source: https://neetcode.io/problems/median-of-two-sorted-arrays/question?list=neetcode150


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    """Finds the median of two sorted arrays in O(log(min(n, m))) time.

    Uses binary search on the smaller array to partition both arrays into two
    halves, ensuring all elements in the left partition are less than or equal
    to all elements in the right partition.

    Args:
        nums1: A sorted list of integers.
        nums2: A sorted list of integers.

    Returns:
        The median of the combined sorted arrays as a float.

    Time Complexity:
        O(log(min(n, m))) where n and m are the lengths of nums1 and nums2.

    Space Complexity:
        O(1) auxiliary space.
    """
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    # Ensure A is always the smaller array
    if len(A) > len(B):
        A, B = B, A

    l, r = 0, len(A) - 1

    while True:
        i = (l + r) // 2  # Partition index for A
        j = half - i - 2  # Partition index for B

        # Handle boundary values near the partition line
        A_left = A[i] if i >= 0 else float("-inf")
        A_right = A[i + 1] if (i + 1) < len(A) else float("inf")
        B_left = B[j] if j >= 0 else float("-inf")
        B_right = B[j + 1] if (j + 1) < len(B) else float("inf")

        # Check if the partition is correct
        if A_left <= B_right and B_left <= A_right:
            # Odd total length
            if total % 2 != 0:
                return min(A_right, B_right)
            # Even total length
            return (max(A_left, B_left) + min(A_right, B_right)) / 2

        # Adjust binary search pointers
        elif A_left > B_right:
            r = i - 1  # Too many elements taken from A
        else:
            l = i + 1  # Too few elements taken from A
