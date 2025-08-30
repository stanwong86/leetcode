class Solution:
    def numDecodings(self, s: str) -> int:
        res = set()
        count = 0
        def loop(leftList, rightStr):
            # print(leftList, rightStr)

            if not rightStr:
                res.add(tuple(leftList))
                return
            
            if 1 <= int(rightStr[0]) <= 26:
                newList = leftList[:]
                newList.append(rightStr[0])
                loop(newList, rightStr[1:])
            
            if 1 <= int(rightStr[:2]) <= 26 and rightStr[0] != '0':
                newList2 = leftList[:]
                newList2.append(rightStr[:2])
                loop(newList2, rightStr[2:])
        
        loop([], s)
        return len(res)

        '''
        1111

        1 1 1 1
        1 1 11
        1 11 1
        11 1 1
        11 11


        '''