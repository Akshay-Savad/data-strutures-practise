class newNode:
	def __init__(self, data):
		self.val = data
		self.left = self.right = None

# Function to insert nodes in level order
def insertLevelOrder(arr, i, n):
	root = None
	# Base case for recursion
	if i < n and arr[i] is not None:
		root = newNode(arr[i])

		# insert left child
		root.left = insertLevelOrder(arr, 2 * i + 1, n)

		# insert right child
		root.right = insertLevelOrder(arr, 2 * i + 2, n)
		
	return root

class Solution:
    def maxLevelSum(self, root):
        if root is None:
            return []

        dfs = [root, None]
        i = 0
        while i < len(dfs):
            if dfs[i] == None:
                if i == len(dfs) - 1: break

                dfs.append(None)
                i += 1
                continue

            if dfs[i].left is not None:
                dfs.append(dfs[i].left)
            if dfs[i].right is not None:
                dfs.append(dfs[i].right)
            i += 1
        
        n = len(dfs)
        import sys
        max_sum = curr_sum = dfs[0].val
        max_index = curr_index = 0
        for i in range(n):
            if dfs[i] == None:
                if max_sum < curr_sum: 
                    max_sum = curr_sum
                    max_index = curr_index
                curr_sum = 0
                curr_index += 1
                continue

            curr_sum += dfs[i].val

        return max_index + 1
    
# Driver Code
if __name__ == '__main__':
    arr = [-100,-200,-300,-20,-5,-10,None]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, 0, n)
    c = Solution()
    print(c.maxLevelSum(root))