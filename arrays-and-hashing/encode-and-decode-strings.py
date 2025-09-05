from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s  # dog -> 3#dog

        return res

    def decode(self, s: str) -> List[str]:
        res, index = [], 0

        while index < len(s):
            j = index

            while s[j] != "#":
                j += 1

            length = int(s[index:j])  # getting the length of the word
            res.append(s[j + 1: j + 1 + length])

            index = j + 1 + length  # Update our index pointer to be after the word

        return res