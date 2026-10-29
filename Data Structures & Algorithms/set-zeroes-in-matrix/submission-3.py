class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # mark rows/cols for zeroing out
        rowZero = any(matrix[0][c] == 0 for c in range(len(matrix[0])))
        colZero = any(matrix[r][0] == 0 for r in range(len(matrix)))
        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[r][c]==0:
                    matrix[r][0]=0
                    matrix[0][c]=0
        # zero out all rows/cols
        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0
        if rowZero:
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        if colZero:
            for r in range(len(matrix)):
                matrix[r][0] = 0