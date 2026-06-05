class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_map,target_map={},{}
        for char in t:
            target_map[char]=target_map.get(char,0)+1
        have,need=0,len(target_map)
        l=0
        res_len=len(s)+1
        res=[-1,-1]
        for r in range(len(s)):
            char=s[r]
            window_map[char]=window_map.get(char,0)+1
            if char in target_map and window_map[char]==target_map[char]:
                have+=1
            while have==need:
                # check if shortest
                if (r-l+1) < res_len:
                    res=[l,r]
                    res_len=r-l+1
                # update l
                window_map[s[l]]-=1
                if s[l] in target_map and window_map[s[l]]<target_map[s[l]]:
                    have-=1
                l+=1
        l,r=res
        if res_len < len(s)+1:
            return s[l:r+1]
        else:
            return ""

