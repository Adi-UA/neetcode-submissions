class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r,t,b=0,len(matrix[0]),0,len(matrix)
        res=[]
        while l<r and t<b:
            # top
            res+=matrix[t][l:r]
            t+=1

            # right
            res+=[matrix[i][r-1] for i in range(t,b)]
            r-=1

            if not t<b or not l<r:
                break
            # bottom
            res+=matrix[b-1][l:r][::-1]
            b-=1

            # left
            res+=[matrix[i][l] for i in range(b - 1, t - 1, -1)] 
            l+=1
        return res