class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]
        for token in tokens:
            print(stack, token)
            if token in ops:
                b,a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        print(stack)
        return int(stack[-1])


        