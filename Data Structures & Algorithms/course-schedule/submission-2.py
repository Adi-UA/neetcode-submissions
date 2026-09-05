class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph as a dict
        # {course1:[prereq,prereq2,..],course2:[],...}
        adjList={c:[] for c in range(numCourses)}
        for c,p in prerequisites:
            adjList[c].append(p)
        path=set()
        def dfs(course):
            if adjList[course]==[]:
                return True
            if course in path:
                return False
            path.add(course)
            for prereq in adjList[course]:
                # if not valid prereq return false
                if not dfs(prereq):
                    return False
            # otherwise this is valid
            adjList[course]=[]
            return True            
        for course in adjList:
            if not dfs(course):
                return False
        return True
        
        