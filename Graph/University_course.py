class Solution:
    def __init__(self) -> None:
        self.graph = {}
        self.stauts = []
        # unvisit = 0, processing = 1,visited = 2
        
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        for i in prerequisites:
            if i[0] in self.graph:
                neighbors = self.graph[i[0]]
            else:
                self.graph[i[0]] = []
                neighbors = self.graph[i[0]]

            neighbors.append(i[1])

        self.stauts = [0 for _ in range(numCourses)]
        
        # temp = None
        # for node in self.graph:
        #     neighbors = self.graph[node]
        #     if neighbors and len(neighbors) != 0:
        #         temp = node

        # if temp is None:    #considering no neighbors for any nodes
        #     return True
        # else:
        #     return self.travers(temp)

        for c in range(0, numCourses):
            if not self.travers(c):
                return False
            
        return True


    def travers(self, node) -> bool:
        if node not in self.graph.keys():
            self.stauts[node] = 2
            return True

        if self.stauts[node] == 1:
            return False
        
        if self.stauts[node] == 2:
            return True
        
        self.stauts[node] = 1
        neighbors = self.graph[node]
        for neighbor in neighbors:
            if neighbor not in self.graph.keys():
                self.stauts[neighbor] = 2
            else:
                return self.travers(neighbor) 
        
        self.stauts[node] = 2
        return True

        

def main():
    obj = Solution()
    num, pre = 2, [[1,0]]
    result1 = obj.canFinish(num, pre)

    num, pre = 20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    result2 = obj.canFinish(num, pre)

    print(result1, result2)

if __name__ == "__main__":
    main()