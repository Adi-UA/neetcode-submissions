class Solution:
    def numDecodings(self, s: str) -> int:
        valid=[str(n) for n in range(1,27)]
        # base case: 1 num
        w1=1
        w2=1 if s[0] in valid else 0
        if len(s) == 1 or not w2: 
            return w2
        # 2+ num
        for i in range(1,len(s)):
            tmp=w2
            if s[i-1:i+1] in valid:
                print("pair valid")
                if s[i]!="0": # both combos (single and pair) valid
                    w2=w1+w2
                else:
                    w2=w1 # only pair valid
            elif s[i] not in valid: # no valid combo e.g. 230
                return 0 
            # if only single valid, keep w2 same
            
            # update w1 as w2
            w1=tmp
        return w2