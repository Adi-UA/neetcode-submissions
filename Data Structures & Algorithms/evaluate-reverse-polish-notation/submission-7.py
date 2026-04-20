class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        # go through tokens
        for c in tokens:
            if c == "+":
                # sum and pop the 2 top values
                stack.append(stack.pop()+ stack.pop())
            elif c == "-":
                b, a= stack.pop(), stack.pop()
                stack.append(a-b)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(c))
        return stack[0]
            
            
        