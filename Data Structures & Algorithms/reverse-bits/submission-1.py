class Solution:
    def reverseBits(self, n: int) -> int:
        # convert to bit and reverse
        b=str(bin(n))[2:]
        b=("0"*(32-len(b)))+b
        # convert to val
        return int(b[::-1],2)

        # non-function solution
        offset=1
        res=0
        for i in range(32):
            res+=int(b[i])*offset
            offset*=2
        return res