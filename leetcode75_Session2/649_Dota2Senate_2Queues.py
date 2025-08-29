class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue = deque()
        dQueue = deque()

        for i, val in enumerate(senate):
            if val == 'R':
                rQueue.append(i)
            else:
                dQueue.append(i)
        
        n = len(senate)
        while rQueue and dQueue:
            r = rQueue.popleft()
            d = dQueue.popleft()

            if r < d:
                rQueue.append(n)
            else:
                dQueue.append(n)

            n += 1

        if rQueue:
            return "Radiant"
        return "Dire"