class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        n = len(nums)
        while i < n:
            j = i + 1
            while j < n:
                if nums[j] < nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                j += 1
            i += 1

        for i in range(n):
            pass    