class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        # create set
        num_set = set(nums)
        # look at each item and remove
        for n in nums:
            if n not in num_set:
                continue
            curr_len = 1
            num_set.remove(n)
            # look for left and remove
            left = n - 1
            while (left in num_set):
                num_set.remove(left)
                curr_len += 1
                left -= 1
            # look for right and remove
            right = n + 1
            while(right in num_set):
                num_set.remove(right)
                curr_len += 1
                right += 1
            # track length of longest list
            longest = max(longest, curr_len)
        return longest