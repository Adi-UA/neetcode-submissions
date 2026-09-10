class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(pos,i):
            # check curr position
            r,c=pos[0],pos[1]
            if board[r][c]!=word[i]:
                return False
            # return if at end of word
            if i==len(word)-1:
                return True
            # check neighbors with dfs
            deltas=[[-1,0],[0,-1],[1,0],[0,1]]
            tmp=board[r][c]
            board[r][c]="#"
            res=False
            for (dr,dc) in deltas:
                row=r+dr
                col=c+dc
                if not 0<=row < len(board) or not 0 <= col < len(board[0]):
                    continue
                if dfs([row,col],i+1):
                    res=True
                    break
            board[r][c]=tmp
            return res
        # go through every value
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs([r,c],0):
                    return True
        return False