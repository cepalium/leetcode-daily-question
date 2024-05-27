"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c in ["(", "[", "{"]:
            stack.append(c)
        if c in [")", "]", "}"] and len(stack) == 0:
            return False
        if c == ")" and stack.pop() != "(":
            return False
        elif c == "]" and stack.pop() != "[":
            return False
        elif c == "}" and stack.pop() != "{":
            return False
        else:
            continue

    if stack:  # there is still opening parenthesis
        return False

    return True


if __name__ == "__main__":
    assert isValid(s="()") == True
    assert isValid(s="()[]{}") == True
    assert isValid(s="(]") == False
