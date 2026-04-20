class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        target_row = None
        l,r = 0,len(matrix) - 1
        while l<=r:
            m = (l+r) //2
            if target < matrix[m][0]:
                # move r down
                r = m - 1
            elif target > matrix[m][-1]:
                # move l up
                l = m + 1
            else:
                target_row = m
                break

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

        