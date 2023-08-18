class solution:
    def doCalculation(self,num):
        sum = 0
        while num > 0:
            digit = num % 10
            num = num // 10
            sum += digit ** 2

        return sum

    # num = doCalculation(100)
    # print(num)

    def isHappy(self, n: int) -> bool:
        num = n
        arr = []
        while num not in arr:
            arr.append(num)
            num = self.doCalculation(num)
            if num == 1:
                return True

        return False
    
s = solution()
print(s.isHappy(19))