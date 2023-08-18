class StockSpanner:
    prices = None; span = None
    def __init__(self):
        self.prices = []
        self.span = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        priceIndex = len(self.prices) - 1
        stack = [1]
        flag = False
        result = 0
        while True:
            if priceIndex <= 0:
                result = len(self.prices)
                break

            if self.prices[priceIndex - 1] > price:
                flag = True
                break
            else:
                stack.append(self.span[priceIndex - 1])
                priceIndex = priceIndex - self.span[priceIndex - 1]
        
        if flag:
            result = 0
            for i in range(len(stack)):
                result += stack[i]

        self.span.append(result)

        return result
        


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
param_2 = obj.next(80)
param_3 = obj.next(60)
param_4 = obj.next(70)
param_5 = obj.next(60)
param_6 = obj.next(75)
param_7 = obj.next(85)