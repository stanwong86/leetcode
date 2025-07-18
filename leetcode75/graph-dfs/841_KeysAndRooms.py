class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        locked = [1] * len(rooms)
        
        def dfs(room_key):
            locked[room_key] = 0
            new_keys = rooms[room_key]
            for key in new_keys:
                if locked[key]:
                    dfs(key)
        
        dfs(0)
        return sum(locked) == 0