class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        # if something it closed, it must be the last opener added to the stack
        for c in s:
            if c in d: # if opener
                stack.append(d[c]) # append the closer
            else: # if closer
                if not stack or c != stack.pop(): #check if stack has items and if expected closer is top of stack
                    return False
        if stack:
            return False
        else:
            return True