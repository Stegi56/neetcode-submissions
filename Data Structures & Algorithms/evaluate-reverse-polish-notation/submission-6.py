class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                elif token == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                else:
                    raise Exception(f"Could not match token: {token} with an operator")
            else:
                stack.append(int(token))        
        return stack[0]
                