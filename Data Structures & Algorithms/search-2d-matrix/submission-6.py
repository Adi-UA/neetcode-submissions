class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        target_row = None
        for i,row in enumerate(matrix):
            if row[0] <= target <= row[-1]:
                target_row = i

        print(target_row)
        # binary search within row
        if target_row is None:
            return False
        else:
            l,r = 0, len(matrix[0])
            while l<=r:
                m = (l+r)//2
                val = matrix[target_row][m]
                print(val)
                if val < target:
                    # move left up
                    l = m+1
                elif val > target:
                    # move right down
                    r=m-1
                else:
                    return True
        return False

        