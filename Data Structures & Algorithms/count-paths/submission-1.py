class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow=[1]*n

        for r in range(m-2,-1,-1):
            currRow=[-1]*n
            currRow[n-1]=1
            for c in range(n-2,-1,-1):
                currRow[c]=currRow[c+1]+prevRow[c]
            print(prevRow)
            prevRow=currRow
        return prevRow[0]