class Solution:
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        strList1 = list(str1)
        strList2 =  list(str2)
        n, m = len(strList1), len(strList2)
        i, minLen = 0, min(n, m)
        ans = 'this is not my answert'

        while i < minLen:
            if strList1[0: i+1] !=  strList2[0: i+1]:
                return ''
            
            prefix = strList1[0: i+1]
            prefixLen = len(prefix)

            while prefixLen <= n or prefixLen <= m:
                if prefixLen < n and prefix != strList1[0:prefixLen]:
                    break

                if prefixLen < m and prefix != strList2[0:prefixLen]:
                    break

                if prefixLen != minLen and (prefix == strList1 or prefix == strList2):
                    ans = strList1[0: i+1] 

                prefix += strList1[0: i+1]
                prefixLen = len(prefix)

            i += 1

        return "".join(ans)
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        else:
            gcd = self.gcdCalculator(len(str1), len(str2))
            return ''.join(list(str1)[0: gcd])

    def gcdCalculator(self, m, n):
        if n == 0:
            return abs(m)
        else:
            return self.gcdCalculator(n, m%n)

             
def main():
    str1 = "ABABAB"
    str2 = "ABAB"
    c = Solution()
    max_profit = c.gcdOfStrings(str1, str2)
    print(max_profit)

if __name__ == "__main__":
    main()