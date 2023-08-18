class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        sList = list(senate)
        i = 0
        while True:
            if len(set(sList)) == 1:
                break

            if i >= len(sList):
                i = 0

            if sList[i] == 'R': 
                if 'D' in sList[i:]:
                    temp = sList[i:]
                    temp.remove('D')
                    sList = sList[:i] + temp

                elif 'D' in sList[:i]:
                    temp = sList[:i]
                    temp.remove('D')
                    sList =  temp + sList[i:]
            else:
                if 'R' in sList[i:]:
                    temp = sList[i:]
                    temp.remove('R')
                    sList = sList[:i] + temp

                elif 'R' in sList[:i]:
                    temp = sList[:i]
                    temp.remove('R')
                    sList =  temp + sList[i:]

            i += 1

        return "Radiant" if next(iter(set(sList))) == 'R' else 'Dire'  
    
def main():
    str1 = "DRRD"
    c = Solution()
    max_profit = c.predictPartyVictory(str1)
    print(max_profit)

if __name__ == "__main__":
    main()