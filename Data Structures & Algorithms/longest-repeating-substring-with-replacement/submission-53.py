class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)<=1:
            return len(s)
        # condition: most freq + count of the rest == k
        l=0
        mp=[0]*26
        res=1
        for r in range(min(len(s),len(s))):
            mp[ord(s[r].lower())-ord('a')]+=1
            i=0
            while sum(mp)-max(mp)>k:
                mp[ord(s[l].lower())-ord('a')]-=1
                l+=1
            res=max(res,sum(mp))
        return res
