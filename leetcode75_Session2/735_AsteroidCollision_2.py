class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # + + do nothing
        # + - delete smaller
        # - + do nothing
        # - - do nothing
        # == delete both
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) > abs(asteroid):
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)
        return stack