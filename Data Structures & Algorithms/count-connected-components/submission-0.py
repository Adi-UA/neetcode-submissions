class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjList
        mp={v:set() for v in range(n)}
        for e in edges:
            mp[e[0]].add(e[1])
            mp[e[1]].add(e[0])
        seen=set()
        def dfs(node):
            print(node,seen)
            seen.add(node)
            for conn in mp[node]:
                if conn in seen:
                    continue
                dfs(conn)
        res=0
        for i in range(n):
            if i not in seen:
                res+=1
                dfs(i)
        return res