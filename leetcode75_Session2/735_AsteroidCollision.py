'''
The trick is to only worry about the left side moving right and right siide moving left asteroids.
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while i < len(asteroids)-1:
            left = asteroids[i]
            right = asteroids[i+1]

            while left >= 0 and right <= 0 and 0 <= i < len(asteroids)-1:
                # print('before - i:', i, ', asteroids:', asteroids)
                if abs(left) == abs(right):
                    asteroids.pop(i)
                    asteroids.pop(i)
                    i -= 1
                elif abs(left) < abs(right):
                    asteroids.pop(i)
                    i -= 1
                else:
                    asteroids.pop(i+1)
                
                # print('i:', i, ', asteroids:', asteroids)
                if 0 <= i < len(asteroids)-1:
                    left = asteroids[i]
                    right = asteroids[i+1]
                else:
                    break
                # print(asteroids)

            
            i += 1
        
        return asteroids
                
