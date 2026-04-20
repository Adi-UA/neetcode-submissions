class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # letters in s
        s_letters = list(s)
        t_letters = list(t)
        for e in s_letters:
            if e in t_letters:
                # remove letter
                t_letters.remove(e)
            else:
                return False
        if len(t_letters) == 0:
            return True
        return False

        