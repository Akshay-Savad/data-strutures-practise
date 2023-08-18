word1 = "abbzccca"
word2 = "babzzczc"
str1_list, str2_list = list(word1), list(word2)
n, m = len(str2_list), len(str2_list)
if n != m:
    # return False
    pass

import collections
obj1 = list(collections.Counter(str1_list).values())
obj1.sort()
obj2 = list(collections.Counter(str2_list).values())
obj2.sort()
if obj2 == obj1:
    print(True)
else:
    print(False)