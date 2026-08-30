class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count=0
        visit=set()
        rows,cols=len(grid),len(grid[0])

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                # for each node in the layer, check all directions
                row,col=q.popleft()
                deltas = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in deltas:
                    if (row+dr in range(rows) and 
                        col+dc in range(cols) and 
                        grid[row+dr][col+dc] == "1" and
                        (row+dr,col+dc) not in visit):
                        q.append((row+dr,col+dc))
                        visit.add((row+dr,col+dc))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] !="0" and (r,c) not in visit:
                    bfs(r,c) # search all land surrounding it
                    count += 1
        return count