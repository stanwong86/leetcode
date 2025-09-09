class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        queue = deque()

        count = 0
        for i, nodes in enumerate(isConnected):
            if i not in visited:
                count += 1
                visited.add(i)
                
                # Initialize Queue
                for j, node in enumerate(nodes):
                    if node == 1:
                        queue.append(j)

                while queue:
                    city = queue.popleft()
                    # print('city', city, 'visited', visited)
                    if city not in visited:
                        for k, val in enumerate(isConnected[city]):
                            if val == 1:
                                queue.append(k)
                                visited.add(city)
            
        return count
