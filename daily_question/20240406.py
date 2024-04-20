"""
1249. Minimum Remove to Make Valid Parentheses (Medium)

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', 
in any positions ) so that the resulting parentheses string is valid 
and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""


def minRemoveToMakeValid(s: str) -> str:
    result_dict = {}  # {index of letter in s: True/False}
    open_parentheses_indices = []  # [index of open parentheses `(` in s]
    # iterate through all letters in s
    for i in range(len(s)):
        # if letter is not parentheses, True
        if s[i] not in ["(", ")"]:
            result_dict[i] = True
            continue
        # if letter is open parentheses, True first
        if s[i] == "(":
            result_dict[i] = True
            open_parentheses_indices.append(i)
            continue
        # if letter is closing parentheses and there are open parentheses, True
        if s[i] == ")" and len(open_parentheses_indices) > 0:
            result_dict[i] = True
            open_parentheses_indices.pop(-1)
            continue
        # if letter is closing parentheses and there is no open parentheses, False
        if s[i] == ")" and len(open_parentheses_indices) <= 0:
            result_dict[i] = False
            continue
    # in the end, the remaining open parentheses are made False
    for i in open_parentheses_indices:
        result_dict[i] = False
    # final result is of all letters of True
    result = ""
    for k, v in result_dict.items():
        if v is True:
            result += s[k]

    return result


if __name__ == "__main__":
    assert minRemoveToMakeValid(s="lee(t(c)o)de)") == "lee(t(c)o)de"
    assert minRemoveToMakeValid(s="a)b(c)d") == "ab(c)d"
    assert minRemoveToMakeValid(s="))((") == ""
