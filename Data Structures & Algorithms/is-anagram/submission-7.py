class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. split both and sort; time:O(nlogn) space: O(n)
        # 2. 2 dictionaries; time and space: O(n)
        # more efficient O(n) space: dictionary count of each letter and then check if all 0
        # return sorted(list(s))==sorted(list(t))
        if len(s)!=len(t):
            return False
        s_dict,t_dict={},{}
        for i in range(len(s)):
            s_dict[s[i]]=s_dict.get(s[i],0)+1
            t_dict[t[i]]=t_dict.get(t[i],0)+1
        print(s_dict,t_dict)
        return s_dict==t_dict
        