class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # var: freq map for t and s; have/need to track valid s substrings
        if len(s)<len(t):
            return ""
        t_mp={}
        for c in t:
            t_mp[c]=t_mp.get(c,0)+1
        have=0
        need=len(t_mp)
        
        # search s
        l=0
        s_mp=defaultdict(int)
        res=[-1,-1]
        for r in range(len(s)):
            s_mp[s[r]]+=1
            if s_mp[s[r]]==t_mp.get(s[r],0):
                have+=1
            while have==need:
                if r-l < res[1]-res[0] or res==[-1,-1]:
                    res=[l,r]
                # remove l
                s_mp[s[l]]-=1
                if s_mp[s[l]]<t_mp.get(s[l],0):
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if res !=[-1,-1] else ""