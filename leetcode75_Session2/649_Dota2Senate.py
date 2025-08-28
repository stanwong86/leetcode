class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rCount = dCount = 0 
        rBan = dBan = 0
        queue = deque(senate)

        for senator in senate:
            if senator == 'R':
                rCount += 1
            else:
                dCount += 1

        while rCount and dCount:
            voter = queue.popleft()
            if voter == 'R':
                if rBan == 0:
                    dBan += 1
                    queue.append(voter)
                else:
                    rBan -= 1
                    rCount -= 1
            else:
                if dBan == 0:
                    rBan += 1
                    queue.append(voter)
                else:
                    dBan -= 1
                    dCount -= 1
            

        if rCount:
            return "Radiant"
        else:
            return "Dire"
        
        