class Solution:

    def encode(self, strs: List[str]) -> str:
        lens=[]
        combined_s=""
        for s in strs:
            lens.append(str(len(s)))
            combined_s+=s
        return ",".join(lens) + "#" + combined_s # e.g. a,bc -> 1,2#abc

    def decode(self, s: str) -> List[str]:
        descriptor=s.split("#")[0]
        if not descriptor:
            return []
        lens=descriptor.split(",")
        res=[]
        pos,len_i=len(descriptor)+1,0
        while len_i<len(lens):
            curr_len=int(lens[len_i])
            res.append(s[pos:pos+curr_len])
            len_i+=1
            pos+=curr_len
        return res



# combine all strings with special char. at the beginning will be a descriptor e.g. 12,2,4,5# which determines the length of each string to decode back. Decoding does a split by the # char and grabs the info from the 0th index