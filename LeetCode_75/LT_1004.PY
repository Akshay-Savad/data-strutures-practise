class Solution:
    def longestOnes(self, nums, k: int) -> int:
        i, n = 0, len(nums)
        zeroCount, firstZero = 0, -1
        while zeroCount < k and i < n:
            if nums[i] == 0:
                zeroCount += 1
                if firstZero == -1:
                    firstZero = i
            i += 1

            
        currLen = maxLength = i
        while i < n:
            if nums[i] == 0:
                if nums[firstZero] == 0:
                    firstZero += 1
                else:
                    while True and firstZero < n:
                        firstZero += 1
                        if nums[firstZero] == 0:
                            firstZero += 1
                            break

                currLen = i - firstZero
                maxLength = max(maxLength, currLen)
            else:
                currLen += 1
                maxLength = max(maxLength, currLen)

            i += 1

        return maxLength + 1

def main():
    arr = [0,0,1,1,1,0,0]
    k = 0
    c = Solution()
    max_profit = c.longestOnes(arr, k)
    print(max_profit)

if __name__ == "__main__":
    main()