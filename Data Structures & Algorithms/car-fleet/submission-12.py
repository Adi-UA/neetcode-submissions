class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort list
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort()
        # for each item from back:
        stack = []
        for p,s in pairs[::-1]:
            # check the time until destination
            stack.append((target - p) / s)
            # if time less than next index remove it
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        