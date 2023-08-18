from typing import List

class Solution:
    def __init__(self) -> None:
        self.graph = dict()
        self.ans = -1

    def addEdge(self, u, v, wt):
        if u not in list(self.graph.keys()):
            self.graph[u] = [[v, wt]]
        else:
            self.graph[u].append([v, wt])

        if v not in list(self.graph.keys()):
            self.graph[v] = [[u, 1/wt]]
        else:
            self.graph[v].append([u, 1/wt])

    def makeGraph(self, equations: List[List[str]], values: List[float]):
        for i in range(len(equations)):
            self.addEdge(equations[i][0], equations[i][1], values[i])

    def dfs(self, nodes, destination, currNode, visitedNodes, curr_ans):
        if currNode in visitedNodes:
            return
        visitedNodes.append(currNode)

        for i in nodes:
            if i[0] == destination:
                self.ans = curr_ans * i[1]
                return
            
            if i[0] in list(self.graph.keys()):
                self.dfs(self.graph[i[0]], destination, i[0], visitedNodes,curr_ans * i[1])
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.makeGraph(equations, values)

        result = []
        self.ans = -1.00000
        for i in queries:
            if i[0] in list(self.graph.keys()):
                self.dfs(self.graph[i[0]], i[1], i[0], [], 1)
            
            result.append(self.ans)
            self.ans = -1.00000

        return result

def main():
    obj = Solution()
    
    # equations = [["a","b"],["b","c"]] 
    # values = [2.0,3.0] 
    # queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

    result2 = obj.calcEquation(equations, values, queries)

    print(result2)

if __name__ == "__main__":
    main()