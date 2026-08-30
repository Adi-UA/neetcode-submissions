class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '#'
        # start with len1,len2,len3...# at the end
        # then combine them by special value like #
        encoded=""
        prefix=""
        for s in strs:
            prefix = prefix + str(len(s)) + ","
            encoded = encoded + "#" + s
        return prefix[:len(prefix)-1] + encoded
    def decode(self, s: str) -> List[str]:
        if s == '#':
            return []
        prefix=s.split("#")[0]
        lengths=[int(length) for length in prefix.split(",")]
        encoded=s[len(prefix):]
        
        res = []
        for l in lengths:
            res.append(encoded[1:l+1]) #exclude starting special char
            encoded=encoded[l+1:]
        return res

        
