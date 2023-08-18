from typing import List
class Solution:
    def __init__(self):
        self.time = 0

    def nearByFreshOranges(self, node, grid, n, m):
        [x, y] = node
        response = []
        
        if x+1 < n and grid[x+1][y] == 1:
            response.append([x+1, y])

        if x-1 >=0 and grid[x-1][y] == 1:
            response.append([x-1, y])

        if y+1 < m and grid[x][y+1] == 1:
            response.append([x, y+1])

        if y-1 >= 0 and grid[x][y-1] == 1:
            response.append([x, y-1])

        return response

    def bfs(self, queue, grid):
        n, m = len(grid), len(grid[0])

        # here queue is dynamic so cannot use range and len
        # this issues is i got in dfs on tree also....
        queueIndex = -1
        while queueIndex < len(queue):
            queueIndex += 1
            if queue[queueIndex] == None:
                if queue[queueIndex-1] == None and queueIndex == len(queue) - 1:
                    self.time -= 1
                    break
                self.time += 1
                queue.append(None)
                continue

            freshOranges = self.nearByFreshOranges(queue[queueIndex], grid, n, m)
            for i in freshOranges:
                [x, y] = i
                grid[x][y] = 2
                if i not in queue:
                    queue.append(i)

        return grid
            
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i, j])

        queue.append(None)
        if len(queue) < 1:
            return 0

        updatedGrid = self.bfs(queue, grid)

        # check any remianing fresh oranges if yes return -1
        for i in updatedGrid:
            for j in i:
                if j == 1:
                    return -1

        return self.time

def main():
    obj = Solution()

    maze = [[2,1,1],[1,1,0],[0,1,1]]
    maze = [[0,2]]
    maze = [[2,1,1],[0,1,1],[1,0,1]]

    result2 = obj.orangesRotting(maze)

    print(result2)

if __name__ == "__main__":
    main()        