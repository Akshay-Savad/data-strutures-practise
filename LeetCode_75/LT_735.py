class Solution:
    def asteroidCollision(self, asteroids):
        nums = []
        for i in asteroids:
            if i > 0:
                nums.append(i)
            else:
                while True:
                    t = nums.pop()
                    ans = abs(t) - abs(i)

                    if ans > 0:
                        nums.append(t)

                    if len(nums) < 0 or ans >= 0:
                        break 
        return nums