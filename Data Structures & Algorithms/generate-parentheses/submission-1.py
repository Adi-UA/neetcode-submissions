class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # list of ( or )
        res = [] # output
        # backtrack
        def backtrack(openN, closedN):
            # return if completed
            if openN == closedN == n:
                res.append("".join(stack))
                return
            # add open parenth first until reaches max
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            # add closed parenth if valid 
            if openN > closedN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0,0)
        return res
            
        