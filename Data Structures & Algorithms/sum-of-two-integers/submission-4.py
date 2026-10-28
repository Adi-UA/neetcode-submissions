class Solution:
    def getSum(self, a: int, b: int) -> int:
        # note: negatives have infinite 1's out front
        mask = 0xFFFFFFFF # 32 1's (8 4-bit hex) -> goal is to cut off value at 32 bits -> so b can equal 0 to exit loop
        max_int = 0x7FFFFFFF # 31 1's (0111 + 28 1's) -> largest positive 32-bit number
        while b!=0:
            carry=(a&b)<<1 # carries shifted by 1
            a=(a^b) & mask # grabs the answer trunacte to 32 bits
            b=carry & mask # same idea
        return a if a <= max_int else ~(a^mask)