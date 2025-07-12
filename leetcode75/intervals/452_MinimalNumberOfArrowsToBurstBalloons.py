class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        prev = 0
        count = 1

        points.sort(key=lambda x: x[1])
        # print(points)
        for i in range(1, len(points)):
            if points[i][0] > points[prev][1]:
                prev = i
                count += 1                

        return count