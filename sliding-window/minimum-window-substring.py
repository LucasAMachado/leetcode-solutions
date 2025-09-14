class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, windowCount = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("infinity")
        l = 0
        have, need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]
            windowCount[c] = 1 + windowCount.get(c, 0)

            if c in countT and windowCount[c] == countT[c]:
                have += 1

            while have == need:

                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                windowCount[s[l]] -= 1
                if s[l] in countT and windowCount[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l:r + 1] if resLen != float("infinity") else ""