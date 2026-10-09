class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False] * (len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                next_i=i+len(w)
                if next_i <= len(s) and s[i:next_i]==w and dp[next_i]==True:
                    dp[i]=True
                    break
        return dp[0]