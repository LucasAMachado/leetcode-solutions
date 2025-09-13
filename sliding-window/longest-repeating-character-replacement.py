class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        countMap = {} # char : freq
        l = 0
        res = 0

        for r in range(len(s)):
            # update countMap
            countMap[s[r]] = 1 + countMap.get(s[r], 0) # 0 is the default value

            while ((r - l + 1) - max(countMap.values())) > k:
                # update our window size
                countMap[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res