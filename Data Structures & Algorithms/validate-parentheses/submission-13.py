class Solution:
    def isValid(self, s: str) -> bool:
        # parentheses dict
        par_dict = {"(": ")", "{":"}", "[":"]"}
        opened_stack = []
        i = 0
        # go through string
        for p in s:
            # store opened
            if p in par_dict:
                opened_stack.append(p)
            # for closed par make sure it matches opened in order
            else:
                # check that all opened parentheses are closed
                if not opened_stack or par_dict[opened_stack[-1]] != p:
                    return False
                # remove paired open parenthesis
                opened_stack.pop(-1)
        return not opened_stack # true if empty; false if not empty
        