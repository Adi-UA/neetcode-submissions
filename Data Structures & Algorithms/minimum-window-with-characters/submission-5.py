class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=r=0
        t_map,window_map={},{}
        shortest=""
        for c in t:
            t_map[c]=t_map.get(c,0)+1
            window_map[c]=0
        # sliding window
        while r < len(s):
            char=s[r]
            if char in t_map:
                window_map[char]+=1
                # check if match
                match=True
                for t_char in t_map:
                    if window_map[t_char]<t_map[t_char]:
                        match=False
                while match:
                    if len(s[l:r+1])<len(shortest) or not shortest:
                        shortest=s[l:r+1]
                    # shift l pointer
                    if s[l] in t_map:
                        window_map[s[l]]-=1
                    l+=1
                    for t_char in t_map:
                        if window_map[t_char]<t_map[t_char]:
                            match=False
            r+=1
        return shortest