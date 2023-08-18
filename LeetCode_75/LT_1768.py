class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i, arr = 0, []
        while i < n and i < m:
            arr.append(word1[i])  
            arr.append(word2[i])
            i += 1
       
        if i < n:
            arr.append(word1[i:n])
        if i < m:
            arr.append(word2[i:m])

        return ''.join(arr)
    
def main():
    word1 = 'ab'
    word2 = 'pqrs'
    c = Solution()
    max_profit = c.mergeAlternately(word1, word2)
    print(max_profit)

if __name__ == "__main__":
    main()