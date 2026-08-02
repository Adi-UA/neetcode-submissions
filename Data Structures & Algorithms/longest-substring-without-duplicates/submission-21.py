class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen,seen_i={},{}
        max_length=0
        for i,c in enumerate(s):
            if c in seen:
                remove_i=seen[c]
                while remove_i in seen_i:
                    seen.pop(seen_i[remove_i])
                    seen_i.pop(remove_i)
                    remove_i-=1
            seen[c]=i
            seen_i[i]=c
            max_length=max(max_length,len(seen))
        return max_length