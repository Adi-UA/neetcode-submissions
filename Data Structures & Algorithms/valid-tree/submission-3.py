class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create adj list
        mp={v:set() for v in range(n)}
        for e in edges:
            mp[e[0]].add(e[1])
            mp[e[1]].add(e[0])
        seen=set()
        print(mp)
        def dfs(node,parent):
            seen.add(node)
            for conn in mp[node]:
                if conn == parent:
                    continue
                if conn in seen and conn is not parent:
                    return False
                seen.add(conn)
                if not dfs(conn,node):
                    return False
            return True
        return dfs(0,None) and len(seen) == n