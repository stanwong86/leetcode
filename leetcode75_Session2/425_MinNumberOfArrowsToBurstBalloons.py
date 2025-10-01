class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))

        prev = 0
        count = 1

        for i in range(1, len(points)):
            if points[prev][1] < points[i][0]:
                count += 1
                prev = i
        
        return count

