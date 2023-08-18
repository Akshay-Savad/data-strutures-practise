class Solution:
    def productExceptSelf(self, nums):
        arr = []
        mult, isZeroArray = nums[0], False
        for i in range(1, len(nums)):
            if nums[i] == 0 and not isZeroArray:
                isZeroArray = True
                continue
            mult *= nums[i] 

        for i in nums:
            if isZeroArray:
                if i != 0:
                    arr.append(0)
                else:
                    arr.append(mult)
                continue

            arr.append(self.giveMeQuotient(mult, i))

        return arr

    def giveMeQuotient(self, divisor: int, dividend: int):
        count = 0 
        a,b = abs(divisor), abs(dividend)
        while a != 0:
            a -= b
            count +=1

        return -count if ((divisor < 0) ^ (dividend < 0)) else count
    
def main():
    arr = [5,9,2,-9,-9,-7,-8,7,-9,10]
    c = Solution()
    max_profit = c.productExceptSelf(arr)
    print(max_profit)

if __name__ == "__main__":
    main()