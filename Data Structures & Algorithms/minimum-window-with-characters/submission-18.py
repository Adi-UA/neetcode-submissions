class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # var: freq map for t and s; have/need to track valid s substrings
        if len(s)<len(t):
            return ""
        t_mp={}
        for c in t:
            t_mp[c]=t_mp.get(c,0)+1
            print(t_mp)
        have=0
        need=len(t_mp)
        
        # search s
        l=0
        s_mp=defaultdict(int)
        res=""
        for r in range(len(s)):
            s_mp[s[r]]+=1
            if s_mp[s[r]]==t_mp.get(s[r],0):
                have+=1
            while have==need:
                if r+1-l < len(res) or not res:
                    res=s[l:r+1]
                # remove l
                s_mp[s[l]]-=1
                if s_mp[s[l]]<t_mp.get(s[l],0):
                    have-=1
                l+=1
        return res