from typing import List


class Solution:
    def minimumMagic(self, n : int, m : int, price : List[int], magical_price : List[int]) -> int:
        # code here
        # sum_price = sum(price)
        sum_magical_price = sum(magical_price)
        if m < sum_magical_price:
            return -1
        
        price_sum = 0
        for i in price:
            price_sum += i
            if  price_sum > m:
                break

        for i in price:
            price_sum += i
            if  price_sum > m:
                break

        


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n, m=IntArray().Input()
        
        
        price=IntArray().Input()
        
        
        magical_price=IntArray().Input()
        
        obj = Solution()
        res = obj.minimumMagic(n, m, price, magical_price)
        
        print(res)