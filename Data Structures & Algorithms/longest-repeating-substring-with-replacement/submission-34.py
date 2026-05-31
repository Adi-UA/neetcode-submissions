class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        counts={}
        longest=0
        for r in range(len(s)):
            counts[s[r]]=1+counts.get(s[r],0)
            while (r-l+1) - max(counts.values()) > k: # if no. substitutions > k, shift left pointer until condition succeeds
                counts[s[l]] -= 1
                l += 1
            longest = max(longest,r-l+1)
        return longest