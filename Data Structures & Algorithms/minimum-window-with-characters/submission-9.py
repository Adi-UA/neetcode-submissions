class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map,window_map={},{}
        for c in t:
            t_map[c]=t_map.get(c,0)+1
            window_map[c]=0
        need=len(t_map)
        have=0
        res,resLen=[-1,-1],float("infinity")
        l=r=0
        # sliding window
        while r < len(s):
            char=s[r]
            if char in t_map:
                window_map[char]+=1
                # update have is applicable
                if window_map[char]==t_map[char]:
                    have+=1
                while have==need:
                    if r-l+1<resLen:
                        res,resLen=[l,r],r-l+1
                    # shift l pointer
                    if s[l] in t_map:
                        if window_map[s[l]]==t_map[s[l]]:
                            have-=1
                        window_map[s[l]]-=1
                    l+=1
            r+=1
        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""