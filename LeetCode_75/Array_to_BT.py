class newNode:
	def __init__(self, data):
		self.data = data
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

# Driver Code
if __name__ == '__main__':
	arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
	n = len(arr)
	root = None
	root = insertLevelOrder(arr, 0, n)
