

"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


class WithoutStringSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        # You can replace by log10. Imagine that we are solving without imports
        length = 2
        while x // 10**length > 0:
            length += 1
        for i in range(1, length // 2 + 1):
            left = (x // (10**(length - i))) % 10
            right = (x % 10**i) // (1 if i == 1 else 10**(i - 1))
            if left != right:
                return False

        return True


class StringSolution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)
        for i in range(l // 2):
            if s[i] != s[l - i - 1]:
                return False
        return True


if __name__ == "__main__":
    test = WithoutStringSolution()
    print(test.isPalindrome(121))
    print(test.isPalindrome(-121))
    print(test.isPalindrome(10))
    print(test.isPalindrome(42))
    print(test.isPalindrome(425171524))
    print(test.isPalindrome(4251771524))

    test = StringSolution()
    print(test.isPalindrome(121))
    print(test.isPalindrome(-121))
    print(test.isPalindrome(10))
    print(test.isPalindrome(42))
    print(test.isPalindrome(425171524))
    print(test.isPalindrome(4251771524))

