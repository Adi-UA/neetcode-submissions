class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l,r,s):
            # looks to left and right of string to check expand palindrome
            res=s[l:r+1]
            while 1<=l<=len(s)-2 and 1<=r<=len(s)-2:
                if s[l-1]!=s[r+1]:
                    break
                l-=1
                r+=1
                res=s[l:r+1] if r-l > len(res) else res
            return res
        # odd
        res=s[0]
        for i in range(1,len(s)-1):
            out=helper(i,i,s) 
            res=out if len(out) > len(res) else res
        # even
        for l in range(0,len(s)-1):
            r=l+1
            if s[l]==s[r]:
                out=helper(l,r,s)
                res=out if len(out) > len(res) else res
        return res