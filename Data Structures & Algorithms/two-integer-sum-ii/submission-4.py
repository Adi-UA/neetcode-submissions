class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start at ends
        i, j = 0, len(numbers) - 1
        # while not intersecting and not target
        while numbers[i] + numbers[j] != target:
            # move left or right based on sum
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        # return 1-indexed indices
        return [i + 1, j + 1]
