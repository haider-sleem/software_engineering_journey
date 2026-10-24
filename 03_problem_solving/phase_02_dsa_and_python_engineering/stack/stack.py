# 1- Source: https://neetcode.io/problems/validate-parentheses/question?list=neetcode150


class Solution:
    def isValid(self, s: str) -> bool:
        """Determines if the input string of brackets is valid.

        A string is valid if all open brackets are closed by the same type
        of close brackets in the correct order.

        Args:
            s (str): A string containing brackets '(', ')', '{', '}', '[' and ']'.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        stack = []
        # Map each closing bracket to its corresponding opening bracket
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping:  # If it's a closing bracket
                # Check if the stack is not empty and the top element matches the expected opening bracket
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False

        return (
            not stack
        )  # Return True if the stack is completely empty (all brackets matched)


# 2- Source:
