class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False] * len(s)
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                next_i=i+len(w)
                if next_i <= len(s) and s[i:next_i]==w:
                    # print(s[i:],w,i,len(w),next_i,s[i:next_i])
                    if next_i==len(s):
                        dp[i]=True
                    elif dp[next_i]==True:
                        dp[i]=True
            print(s[i:],dp[i])
        return dp[0]