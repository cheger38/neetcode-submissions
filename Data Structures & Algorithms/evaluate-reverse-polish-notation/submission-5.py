def operation(op, left, right):
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right
    elif op == "/":
        return int(left/right)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] in "+-*/":
                right = stack.pop()
                left = stack.pop()
                val = operation(tokens[i], left, right)
                stack.append(val)
            else:
                stack.append(int(tokens[i]))

            print(stack)
                
            i += 1

        print(stack)
        return stack[0]




            
