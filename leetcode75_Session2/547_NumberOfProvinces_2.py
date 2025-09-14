class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()

        def dfs(city):
            if city in visited:
                return
            visited.add(city)

            neighbors = isConnected[city]
            for i in range(len(neighbors)):
                if neighbors[i] == 1 and i not in visited:
                    dfs(i)

        for i in range(len(isConnected)):
            if i in visited:
                continue
            
            provinces += 1
            dfs(i)
        
        return provinces