class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                a = stack.pop()
                if abs(a) == abs(asteroid):
                    asteroid = 0
                    break
                elif abs(a) > abs(asteroid):
                    stack.append(a)
                    asteroid = 0
                    break
            
            if asteroid != 0:
                stack.append(asteroid)
        return stack
