class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        freq_hash={}
        for r in range(len(s)):
            freq_hash[s[r]]=1+freq_hash.get(s[r],0)
            if (r-l+1) - max(freq_hash.values()) > k: # if no. substitutions > k, shift left pointer
                freq_hash[s[l]] -= 1
                l += 1
            longest = r-l+1
        return longest