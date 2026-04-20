class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize stack -> later add tuples [(i, t)]
        tempStack = []
        res = [None] * len(temperatures)
        for i, t in enumerate(temperatures):
            if i == 0:
                tempStack.append((i,t))
            else:
                # compare to temp of top
                # if greater pop out top and add to res
                # keep going until not greater
                while tempStack and t > tempStack[-1][1]:
                    lower_i = tempStack[-1][0]
                    days_diff = i - lower_i

                    res[lower_i] = days_diff
                    # pop out top
                    tempStack.pop()
                # add to top of list
                tempStack.append((i,t))
            print(tempStack)
        # at end of input list
        if i == len(temperatures) - 1:
            # put 0 for all tempStack indices
            while len(tempStack) > 0:
                # make 0
                res[tempStack[-1][0]] = 0
                # pop out
                tempStack.pop()
        return res
            


        