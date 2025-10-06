class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        countD = defaultdict(int)
        routes = {}
        visited = set()
        res = []

        for i in range(numCourses):
            routes[i] = []
            visited.add(i)

        for course, prereq in prerequisites:
            routes[prereq].append(course)
            countD[course] += 1
            try:
                visited.remove(course)
            except KeyError:
                pass
        
        queue = deque(visited)
        
        while queue:
            prereq = queue.popleft()
            res.append(prereq)

            for course in routes[prereq]:
                if course in visited:
                    continue
                
                countD[course] -= 1
                if countD[course] == 0:
                    queue.append(course)
                    visited.add(course)

        if len(visited) != numCourses:
            return []
        return res