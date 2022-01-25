# Palindrome Number

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.

# Similar to 1332.py.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        return True if x == x[::-1] else False