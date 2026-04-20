class Solution:
    def isValid(self, s: str) -> bool:
        # parentheses dict
        par_dict = {"(": ")", "{":"}", "[":"]"}
        opened = []
        i = 0
        # go through string
        while i < len(s):
            print(i)
            # store opened
            if s[i] in par_dict:
                opened.append(s[i])
                i += 1
                print(opened)
            # for closed par make sure it matches opened in order
            else:
                # invalid if no opened parentheses
                if len(opened) == 0:
                    return False
                # check that all opened parentheses are closed
                if par_dict[opened[-1]] == s[i]:
                    # remove paired open parenthesis
                    opened.pop(-1)
                    print(opened)
                    i += 1
                else:
                    return False
        if len(opened) == 0:
            return True
        else:
            return False
        