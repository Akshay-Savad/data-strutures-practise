class newNode:
	def __init__(self, data):
		self.val = data
		self.left = self.right = None

# Function to insert nodes in level order
def insertLevelOrder(arr, i, n):
	root = None
	# Base case for recursion
	if i < n:
		root = newNode(arr[i])

		# insert left child
		root.left = insertLevelOrder(arr, 2 * i + 1, n)

		# insert right child
		root.right = insertLevelOrder(arr, 2 * i + 2, n)
		
	return root

class Solution:
    def rightSideView(self, root):
        return self.bfs(root)

    def bfs(self, root):
        if root is None:
            return []
        temp_arr = [root, None]
        arr = []
        i = 0
        while i < len(temp_arr):
            if temp_arr[i] == None:
                if i == len(temp_arr) - 1:
                    break

                temp_arr.append(None)
                i += 1
                continue

            if temp_arr[i].left is not None:
                temp_arr.append(temp_arr[i].left)

            if temp_arr[i].right is not None:
                temp_arr.append(temp_arr[i].right)

            i += 1

        n = len(temp_arr)
        for i in range(n):
            if temp_arr[i] == None:
                arr.append(temp_arr[i - 1].val)

        return arr
    
def main(root):
    o = Solution()
    arr = o.rightSideView(root)
    print(arr)

# Driver Code
if __name__ == '__main__':
    arr = []
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, 0, n)
    
    main(root)
