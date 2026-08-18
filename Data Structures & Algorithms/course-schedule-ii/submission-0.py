class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adjList[course].append(pre)

        # a course has 3 possiblilties:
        # visited -> crs has been added to the output
        # visiting -> crs not added to the output
        # unvisited -> crs not added to the output
    
        visit, cycle = set(), set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in adjList[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output


        