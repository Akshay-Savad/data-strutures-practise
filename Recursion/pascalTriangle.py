class Solution:
    def pascalTriangle(self, num:int) -> list:
        if num == 0: return [1]

        resultList = self.pascalTriangle(num - 1)
        for i in range(len(resultList) - 1):
            resultList[i] += resultList[i+1]

        return [1] + resultList

import math

def main():
    num = 0    
    ob=Solution()
    ans=ob.pascalTriangle(num)
    
    print(ans)


if __name__ == "__main__":
    main()