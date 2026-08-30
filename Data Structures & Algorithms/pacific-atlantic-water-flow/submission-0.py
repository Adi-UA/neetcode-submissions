class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows=len(heights)
        cols=len(heights[0])
        def bfs(starts):
            visit=set(starts)
            q=deque(starts)
            while q:
                r,c=q.popleft()
                deltas=[[0,-1],[-1,0],[0,1],[1,0]]
                for (dr,dc) in deltas:
                    # add stuff that can flow to ocean
                    if ((r+dr) in range(rows) and
                       (c+dc) in range(cols) and
                       (r+dr,c+dc) not in visit and
                       heights[r][c] <= heights[r+dr][c+dc]): # new will flow to existing
                        visit.add((r+dr,c+dc))
                        q.append((r+dr,c+dc))
            return visit
        pacific=bfs([(r,0) for r in range(rows)]+[(0,c) for c in range(cols)])
        atlantic=bfs([(r,cols-1) for r in range(rows)]+[(rows-1,c) for c in range(cols)])
        return [[r,c] for r,c in atlantic&pacific]
