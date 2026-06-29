def isMatching(openB, closeB):
    if openB == '(' and closeB == ')':
        return True
    if openB == '{' and closeB == '}':
        return True
    if openB == '[' and closeB == ']':
        return True

    return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            elif stack and isMatching(stack[-1], c):
                stack.pop()
            else:
                return False

        return not stack


