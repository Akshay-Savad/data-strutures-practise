class Solution:
    def longestSubarray(self, nums) -> int:
        i, n = 0, len(nums)
        lastZero, maxCount, windowOpen = -1, 0, 0
        while i < n:
            if nums[i] == 0:
                if lastZero != -1:
                    windowOpen = lastZero + 1 
                
                lastZero = i
            maxCount = max(maxCount, i - windowOpen)

            i += 1

        if lastZero == -1:
            return n - 1
        else:
            return max(maxCount, n - windowOpen)

def main():
    arr = [1,1,0,1]
    c = Solution()
    max_profit = c.longestSubarray(arr)
    print(max_profit)

if __name__ == "__main__":
    main()        