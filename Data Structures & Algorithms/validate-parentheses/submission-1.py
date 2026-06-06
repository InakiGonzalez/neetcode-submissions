class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesDict = {')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            if c not in parenthesesDict:
                stack.append(c)
                continue

            if not stack or stack[-1] != parenthesesDict[c]:
                return False
            stack.pop()
                
        return not stack
