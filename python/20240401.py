"""
58. Length of Last Word (Easy)
Given a string s consisting of words and spaces, 
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


def lengthOfLastWord(s: str) -> int:
    words = s.strip().split(" ")
    last_word = words[-1]
    return len(last_word)


if __name__ == "__main__":
    assert lengthOfLastWord(s="Hello World") == 5
    assert lengthOfLastWord(s="   fly me   to   the moon  ") == 4
    assert lengthOfLastWord(s="luffy is still joyboy") == 6
