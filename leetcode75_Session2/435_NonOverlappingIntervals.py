class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        prev = 0
        removeCount = 0
        
        print(intervals)
        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                removeCount += 1
            else:
                prev = i

        return removeCount