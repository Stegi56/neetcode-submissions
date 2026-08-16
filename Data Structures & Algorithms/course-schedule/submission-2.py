class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps = {course: [] for course in range(numCourses)}

        for pre in prerequisites:
            deps[pre[0]].append(pre[1])

        visited = set()
        def dfs(course) -> bool:
            if course in visited:
                return False
            if deps[course] == []:
                return True

            valid = True
            visited.add(course)
            for pre in deps[course]:
                valid = valid and dfs(pre)
            visited.remove(course)
            if valid:
                deps[course] = []
            return valid

        res = True
        for course in range(numCourses):
            res = res and dfs(course)
        
        return res
            


