class Solution:
    def NearByDuplicatesGoogle(self, string:str):
        if len(string) == 1: return string

        if string[0] == string[1]: return self.NearByDuplicatesGoogle(string[1:])

        # my first implmentation, 
        # rather than passing that single char to next function, directly return that char here
        else: 
        #     string1 = self.NearByDuplicatesGoogle(string[0])
            string1 = string[0]
            string2 = self.NearByDuplicatesGoogle(string[1:])
            return string1 + string2

import math

def forLoopApproach(string):
    n, i = len(string), 0
    stack = []
    while i < n - 1:
        if string[i] == string[i+1]:
            i += 1
        stack.append(string[i])
        i += 1
        
    return stack


def main():
    string = "myllllccoo"    
    ob=Solution()
    ans=ob.NearByDuplicatesGoogle(string)

    print(forLoopApproach(string))
    
    print(ans)


if __name__ == "__main__":
    main()