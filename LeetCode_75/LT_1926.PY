from typing import List

class Node:
    location = []
    steps = int()

    def __init__(self, location, steps):
        self.location = location
        self.steps = steps

class Solution:
    def __init__(self):
        self.queue = []
        self.minSteps = []
    
    def isNodeValid(self, x, y, n, m, maze):
        if x < 0 or y < 0:
            return False
        if x >= n or y >= m:
            return False
        if maze[x][y] == '+' or maze[x][y] == 'visited':
            return False
        return True

    def isBoundryCell(self, x, y, n, m, entrance):
        if [x, y] == entrance:
            return False
        if x == n-1:
            return True 
        if y == m-1:
            return True
        if x == 0 or y == 0:
            return True
        return False
    
    def appendNodes(self, x, y, maze, n, m, node, entrance):
        if self.isNodeValid(x, y, n, m, maze):
            # check if we reached to border
            if self.isBoundryCell(x, y, n, m, entrance):
                self.minSteps.append(node.steps + 1)
            
            # create Node and add it to queue
            new_node = Node([x, y], node.steps + 1)
            self.queue.append(new_node)
            maze[x][y] = 'visited'

        return maze

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        firstNode = Node(entrance, 0)
        self.queue.append(firstNode)
        n = len(maze)
        m = len(maze[0])

        while len(self.queue) > 0:
            node = self.queue.pop(0)
            x = node.location[0]
            y = node.location[1]
            maze = self.appendNodes(x + 1, y, maze, n, m, node, entrance)
            maze = self.appendNodes(x - 1, y, maze, n, m, node, entrance)
            maze = self.appendNodes(x, y + 1, maze, n, m, node, entrance)
            maze = self.appendNodes(x, y - 1, maze, n, m, node, entrance)

            
        if len(self.minSteps) == 0:
            return -1
        else:
            return min(self.minSteps)

def main():
    obj = Solution()

    maze = [["+",".","+","+","+","+","+"],
            ["+",".","+",".",".",".","+"],
            ["+",".","+",".","+",".","+"],
            ["+",".",".",".","+",".","+"],
            ["+","+","+","+","+",".","+"]]
    entrance = [0,1]

    result2 = obj.nearestExit(maze, entrance)

    print(result2)

if __name__ == "__main__":
    main()        
