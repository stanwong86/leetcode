class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            # beginning
            if i == 0:
                if sum(flowerbed[0:2]) == 0:
                    n -= 1
                    flowerbed[0] = 1
            
            elif i == len(flowerbed)-1:
                return False
            
            # end
            elif i == len(flowerbed)-2 and sum(flowerbed[0:2]) == 0:
                n -= 1
                flowerbed[len(flowerbed)-1] = 1

            # middle
            elif sum(flowerbed[i:i+3]) == 0:
                flowerbed[i+1] = 1
                i += 1
                n -= 1
            
            if n <= 0:
                return True
        
        return False

