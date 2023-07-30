
"""
20. Valid Parentheses
Problem link: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

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

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        math_parentheses = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        opened_list = []
        for i in s:
            if i in math_parentheses:
                opened_list.append(i)
            elif opened_list and math_parentheses[opened_list[-1]] == i:
                opened_list.pop()
            else:
                return False

        return not bool(opened_list)


if __name__ == "__main__":
    test = Solution()
    print(test.isValid("()"))
    print(test.isValid("()[]{}"))
    print(test.isValid("(]"))
    print(test.isValid("]]"))
