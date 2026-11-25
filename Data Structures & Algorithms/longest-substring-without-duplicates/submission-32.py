class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        l,r=0,0
        mp=defaultdict(int)
        res=1
        curr=0
        while r<len(s):
            mp[s[r]]+=1
            curr+=1
            # if no duplicates then use curr
            if mp[s[r]]==1:
                res=max(res,curr)
            # else duplicates: move l up until no duplicates
            else:
                while mp[s[r]]>1:
                    mp[s[l]]-=1
                    l+=1
                    curr-=1
            r+=1
        return res