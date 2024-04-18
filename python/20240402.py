"""
205. Isomorphic Strings (Easy)

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s 
can be replaced to get t.

All occurrences of a character must be replaced with 
another character while preserving the order of characters. 
No two characters may map to the same character, 
but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""


def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # here: len(s) == len(t)
    check_dict = {}
    for i in range(len(s)):
        # if letter s is new
        if s[i] not in check_dict.keys():
            check_dict[s[i]] = t[i]
        # else letter s is in s_dict, check if letter t is different then False
        if t[i] != check_dict[s[i]]:
            return False

    # if s has 2 letters mapping to the same letter from t, return False
    key_set = set(check_dict.keys())
    value_set = set(check_dict.values())
    if len(key_set) != len(value_set):
        return False

    return True


if __name__ == "__main__":
    assert isIsomorphic(s="egg", t="add") == True
    assert isIsomorphic(s="foo", t="bar") == False
    assert isIsomorphic(s="paper", t="title") == True
    assert isIsomorphic(s="badc", t="baba") == False
