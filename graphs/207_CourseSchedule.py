'''
25 minutes
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        routes = {i: [] for i in range(numCourses)}
        countD = defaultdict(int) # key = course, value = prereq count
        queue = deque()
        for course, prereq in prerequisites:
            # b is prereq of a
            countD[course] += 1
            routes[prereq].append(course)
        
        # courses without prereqs
        for i in range(numCourses):
            if i not in countD:
                queue.append(i)
                visited.add(i)

        while queue:
            course = queue.popleft()
            
            for prereq in routes[course]:
                if prereq in visited:
                    continue

                countD[prereq] -= 1
                if countD[prereq] == 0:
                    queue.append(prereq)
                    visited.add(prereq)

        return len(visited) == numCourses
        