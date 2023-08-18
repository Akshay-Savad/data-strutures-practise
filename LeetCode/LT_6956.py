from typing import List

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        backUp = [i for i in nums]
        def checkPrevOfNext(i):
            if backUp[i] == maxFreqNum:
                return True
            if i < n - 1 and i >= 1:
                if backUp[i-1] == maxFreqNum or  backUp[i+1] == maxFreqNum:
                    return True
                else:
                    return False
                
            if i == 0:
                if backUp[n-1] == maxFreqNum or  backUp[i+1] == maxFreqNum:
                    return True
                else:
                    return False
            
            if i == n-1:
                if backUp[i-1] == maxFreqNum or  backUp[0] == maxFreqNum:
                    return True
                else:
                    return False
            
            return True
        
        
        import collections
        c, n = collections.Counter(nums), len(nums)
        c_values = c.values()
        maxFreq = max(list(c_values))
        if n == maxFreq:
            return 0
        
        for i in c:
            if c[i] == maxFreq:
                maxFreqNum = i
                break
        
        counter = 0
        while True:
            backUp = [i for i in nums]
            for i in range(n):
                if checkPrevOfNext(i):
                    nums[i] = maxFreqNum
            
            counter += 1
            if sum(nums) == n * maxFreqNum:
                break
                
        return counter
                
def main():
    obj = Solution()

    s= [2,1,3,3,2]

    result2 = obj.minimumSeconds(s)

    print(result2)

if __name__ == "__main__":
    main()   