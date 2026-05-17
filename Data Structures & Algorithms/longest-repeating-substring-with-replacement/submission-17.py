class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)<=1:
            return len(s)
        # if string > 1
        longest=1
        for i in range(len(s)):
            replacements=0
            char=s[i]
            for j in range(i+1,len(s)):
                if s[j] != char:
                    replacements+=1
                if replacements > k:
                    j-= 1
                    replacements-=1
                    break
            leftover = k - replacements
            curr_longest = min(len(s),j-i+1+leftover)
            print(curr_longest)
            longest=max(longest,curr_longest)
            print("next")
        return longest

