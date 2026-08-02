class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.combos = []
        self.combo = []

        def combine(start, running_total):
            for i in range(start, len(nums)):
                if running_total + nums[i] > target:
                    return
                self.combo.append(nums[i])
                if running_total + nums[i] == target:
                    self.combos.append(list(self.combo))
                else:
                    combine(i, running_total + nums[i])
                self.combo.pop()

        combine(0, 0)
        return self.combos