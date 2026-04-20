class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers init at begin and end points
        i, j = 0, len(s) - 1
        # while they don't intersect
        while i < j:
            # left valid char (have not intersected)
            while i < j and not s[i].isalnum():
                i+= 1
            # right valid char
            while i < j and not s[j].isalnum():
                j -= 1
            # compare
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

        