
"""
14. Longest Common Prefix
Problem link: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for string in strs[1::]:
                if i >= len(string):
                    return prefix
                if string[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix


if __name__ == "__main__":
    test = Solution()
    print(test.longestCommonPrefix(["flower", "flow", "flight"]))
    print(test.longestCommonPrefix(["dog", "racecar", "car"]))
