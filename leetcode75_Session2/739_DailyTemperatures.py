class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = len(temperatures) * [0]

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                lastIndex = stack.pop()
                res[lastIndex] = i - lastIndex
                
            stack.append(i)
        
        return res