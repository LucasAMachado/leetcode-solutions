class Solution2(object):
    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """

        f_string = []

        for c in s:
            if c.isalnum():
                f_string.append(c.lower())

        if len(f_string) % 2 != 0:
            return False

        left, right = 0, len(f_string) - 1

        while left <= right:
            if f_string[left] != f_string[right]:
                return False

            left += 1
            right -= 1

        return True

# Better Solution 
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlpha(s[l]):
                l += 1

            while r > l and not self.isAlpha(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True

    def isAlpha(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))