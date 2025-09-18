class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:

            # we see a closing bracket
            if c in closedToOpen:
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            # we see an open bracket
            else:
                stack.append(c)

        return len(stack) == 0




