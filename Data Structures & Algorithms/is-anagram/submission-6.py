class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sizeS, sizeT = len(s), len(t)
        if sizeS != sizeT:
            return False
        
        ENGLISH_ALPHABETS = 26
        cS, cT = [0]*ENGLISH_ALPHABETS,[0]*ENGLISH_ALPHABETS
        for i in range(sizeS):
            charS = ord(s[i]) - ord('a')
            charT = ord(t[i]) - ord('a')
            cS[charS] += 1
            cT[charT] += 1
        
        for i in range(ENGLISH_ALPHABETS):
            if cS[i] != cT[i]:
                return False
        
        return True


        