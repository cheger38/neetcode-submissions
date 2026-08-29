class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {'+', '-', '*', '/'}:
                stack.append(int(t))
                continue

            right = stack.pop()
            left = stack.pop()

            if t == '+':
                stack.append(left + right)
            elif t == '-':
                stack.append(left - right)
            elif t == '*':
                stack.append(left * right)
            elif t == '/':
                stack.append(int(left / right))

        return stack[-1]