class Solution:
    def equalPairs(self, grid) -> int:
        n = len(grid)
        count = 0
        for i in range(n):
            k, flag = 0, True
            while k < n:
                if grid[i][k] != grid[k][i]:
                    flag = False
                    break
                k += 1
                if flag: count += 1
        return count
    
def main():
    arr = [[3,2,1],[1,7,6],[2,7,7]]
    c = Solution()
    max_profit = c.equalPairs(arr)
    print(max_profit)

if __name__ == "__main__":
    main()