class Solution:
    def coinChange(self, coins, amount: int) -> int:
        coins.sort()
        
        arr = [0 for _ in range(amount+1)]
        n = len(arr)
        for i in coins:
            arr = self.coinChangeHelper(i, arr, n, True if i == coins[0] else False)
        return arr.pop()

    def coinChangeHelper(self, i, arr, length, isFirstRoundFlag = False):
        copyarr = arr.copy()
        if isFirstRoundFlag:
            # go from first value
            arr[0] = 1
            index = 0
            while index < length:
                if index % i == 0:
                    arr[index] = 1
                else:
                    arr[index] = 0
                index += 1
        else:
            index = i
            while index < length:
                arr[index] = copyarr[index] + arr[index - i]
                index += 1

        return arr

def main():
    coins = [1, 2, 5]
    amount = 5

    coins = [3]
    amount = 2

    # coins = [1]
    # amount = 0
    c = Solution()
    max_profit = c.coinChange(coins, amount)
    print(max_profit)

if __name__ == "__main__":
    main()