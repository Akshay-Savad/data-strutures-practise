from typing import List 
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans, n = [], len(potions)

        def counterNumbers(targetNumber) -> int:
            i = 0
            if targetNumber < potions[0]:
                return 0 
            while i < n:
                if potions[i] == targetNumber:
                    return n-i-1  
                if potions[i] < targetNumber and targetNumber < potions[i+1]:
                    return n-i
                i += 1

        for i in spells:
            targetNumber = success / i
            ans.append(counterNumbers(targetNumber))
        
        return ans
def main():
    obj = Solution()

    s= [3,1,2]
    p = [8,5,8]
    ss = 7

    result2 = obj.successfulPairs(s, p, ss)

    print(result2)

if __name__ == "__main__":
    main()   