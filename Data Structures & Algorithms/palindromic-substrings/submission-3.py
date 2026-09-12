class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(l,r,s):
            # looks to left and right of string to check expand palindrome
            res=0
            while 0<=l<=len(s)-1 and 0<=r<=len(s)-1 and s[l]==s[r]:
                l-=1
                r+=1
                res+=1
            return res
        # odd
        res=0
        for i in range(len(s)):
            res+=helper(i,i,s) 
        # even
        for l in range(0,len(s)-1):
            r=l+1
            if s[l]==s[r]:
                res+=helper(l,r,s)
        return res