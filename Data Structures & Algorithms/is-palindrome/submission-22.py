class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers init at begin and end points
        i, j = 0, len(s) - 1
        # while they don't intersect
        while i < j:
            # left valid char (part of string and alnum)
            while i < len(s) and not s[i].isalnum():
                i+= 1
            # right valid char (part of string and alnum)
            while j >= 0 and not s[j].isalnum():
                j -= 1
            # compare
            if i <= len(s) and j >= 0:
                if s[i].lower() != s[j].lower():
                    return False
            i += 1
            j -= 1
        return True

        