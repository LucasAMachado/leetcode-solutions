class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        # To store the frequency of each character
        freq = [0] * 26

        # Count the freq of chars in 's'
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # Check if we have the same chars in t as in s
        for char in t:
            freq[ord(char) - ord('a')] -= 1
            if freq[ord(char) - ord('a')] < 0:
                return False


        return True

