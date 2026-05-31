class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        letters = {}
        seen = {}

        # Initialize both frequency maps for the first window
        for i in range(len(s1)):
            letters[s1[i]] = letters.get(s1[i], 0) + 1
            seen[s2[i]] = seen.get(s2[i], 0) + 1

        if seen == letters:
            return True
        # for all possible r indices
        for r in range(len(s1), len(s2)):
            # add new right
            seen[s2[r]]=seen.get(s2[r],0)+1
            # remove left char and update pointer
            l = r - len(s1)
            seen[s2[l]] -= 1
            if seen[s2[l]]==0:
                del seen[s2[l]]
            if seen==letters:
                return True
        return False
