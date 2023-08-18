class SmallestInfiniteSet:
    def __init__(self):
        # considering its as reverse priorityqueue and maintaining it as min heap
        self.priorityQueue = [] 

    def popSmallest(self) -> int:
        n = len(self.priorityQueue) 
        if n < 1:
            self.priorityQueue = [1]
            return 1

        i = 0
        elemToBeAdded = n + 1
        while i < n:
            if self.priorityQueue[i] != i + 1:
                elemToBeAdded = i + 1
            i += 1

        self.priorityQueue.append(elemToBeAdded)
        self.heapify(n)
        return elemToBeAdded
    
    def heapify(self, index):
        # parentIndex = (index-1)//2
        # if index >= 0 and index < len(self.priorityQueue) and parentIndex >= 0 and parentIndex < len(self.priorityQueue):
        #     if self.priorityQueue[index] < self.priorityQueue[parentIndex]:
        #         self.priorityQueue[parentIndex], self.priorityQueue[index] = self.priorityQueue[index], self.priorityQueue[parentIndex]
        #         self.heapify(parentIndex)
        self.priorityQueue.sort()

    def addBack(self, num: int) -> None:
        if len(self.priorityQueue) < 1 or num not in self.priorityQueue:
            return None

        index = self.priorityQueue.index(num)
        self.priorityQueue.pop(index)
        self.topBottomHeapify(index)

    def topBottomHeapify(self, index):
        leftChild, rightChild = (2 * index) + 1, (2 * index) + 2
        
        if leftChild < len(self.priorityQueue) and self.priorityQueue[leftChild] > self.priorityQueue[index]:
            self.priorityQueue[leftChild], self.priorityQueue[index] = self.priorityQueue[index], self.priorityQueue[leftChild]
            self.topBottomHeapify(leftChild)
            return

        if rightChild < len(self.priorityQueue) and self.priorityQueue[rightChild] < self.priorityQueue[index]:
            self.priorityQueue[rightChild], self.priorityQueue[index] = self.priorityQueue[index], self.priorityQueue[rightChild]
            self.topBottomHeapify(rightChild)
            return

def main():
    c = SmallestInfiniteSet()
    print(c.popSmallest())
    print(c.popSmallest())
    c.addBack(3)
    print(c.popSmallest())
    c.addBack(2)
    print(c.popSmallest())
    print(c.popSmallest())

    # for i in range(1, 10):
    #     print(c.popSmallest())

if __name__ == "__main__":
    main()


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)