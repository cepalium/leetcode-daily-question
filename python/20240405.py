"""
1544. Make The String Great (Easy)

Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters 
s[i] and s[i + 1] where:

* 0 <= i <= s.length - 2
* s[i] is a lower-case letter and s[i + 1] is the same letter but 
in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters 
that make the string bad and remove them. You can keep doing this 
until the string becomes good.

Return the string after making it good. The answer is guaranteed 
to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, 
both will result "leEeetcode" to be reduced to "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. 
For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"
"""


def makeGood(s: str) -> str:
    if len(s) == 0:
        return ""

    letters = list(s)
    stack = []
    while letters:
        # if stack is empty, add 1st letter from s to stack
        if len(stack) == 0:
            stack.append(letters.pop(0))
            continue
        # stack is not empty
        first_letter = letters.pop(0)
        s = stack[-1]
        # if good pair of adjacent letters
        if (first_letter.islower() and s.islower()) or (
            first_letter.isupper() and s.isupper()
        ):
            stack.append(first_letter)
        elif first_letter.lower() != s.lower():
            stack.append(first_letter)
        # bad pair of adjacent letters, remove both from stack and letters
        else:
            stack.pop()

    result = "".join(stack)
    return result


if __name__ == "__main__":
    assert makeGood(s="leEeetcode") == "leetcode"
    assert makeGood(s="abBAcC") == ""
    assert makeGood(s="s") == "s"
    assert makeGood(s="Pp") == ""
