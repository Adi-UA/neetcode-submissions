class Solution:
    def encode(self, strs: List[str]) -> str:
        # empty string output init
        out = ""
        # go through each s in strs
        for s in strs:
            # add to output with length,#, and value
            out += str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        i,j = 0,0
        out = []
        while i < len(s):
            while s[i] != "#":
                i+=1
            length = int(s[j:i])
            word = s[i+1:i+1+length]
            out.append(word)

            i=j=i+1+length

        return out