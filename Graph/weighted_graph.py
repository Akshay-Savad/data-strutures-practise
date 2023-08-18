# weighted graph using adjuceny list and dict
# dict = {
#     key: [[node1, vale1], [node2, val2]]
# }

def addEdge(adj, u, v, wt):
	
    if u not in list(adj.keys()):
        adj[u] = [[v, wt]]
    else:
        adj[u].append([v, wt])
	
    if v not in list(adj.keys()):
        adj[v] = [[u, 1/wt]]
    else:
        adj[v].append([u, 1/wt])
    
    return adj

# Print adjacency list representation of graph
def printGraph(adj, V):
	
	v, w = 0, 0
	for u in range(V):
		print("Node", u, "makes an edge with")

		for it in adj[u]:
			v = it[0]
			w = it[1]
			print("\tNode", v, "with edge weight =", w)
			
		print()

# Driver code
if __name__ == '__main__':
	
	V = 5
	adj = [[] for i in range(V)]
	adj1 = {}

	adj1 = addEdge(adj1, 0, 1, 10)
	adj1 = addEdge(adj1, 0, 4, 20)
	adj1 = addEdge(adj1, 1, 2, 30)
	adj1 = addEdge(adj1, 1, 3, 40)
	adj1 = addEdge(adj1, 1, 4, 50)
	adj1 = addEdge(adj1, 2, 3, 60)
	adj1 = addEdge(adj1, 3, 4, 70)

	# printGraph(adj, V)
	for i in adj1:
		print(i, adj1[i])

# This code is contributed by mohit kumar 29
