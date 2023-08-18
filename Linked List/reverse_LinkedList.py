import ctypes
class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

class LinkedList():
    def __init__(self) -> None:
        self.start = None

    def showLL(self):
        print("\n--")
        printVal = self.start
        while printVal is not None:
            print(printVal.data, end=" ")
            printVal = printVal.next

    def insert_At_Last(self, Node: Node):     # General Method to add Node to Last Position of DLL
        if Node.data == None:
            print("Data is None")
            return
        
        Node.next = None
        if self.start is None:
            self.start = Node
            return
        
        currNode = self.start
        while currNode.next is not None:
            currNode = currNode.next

        currNode.next = Node

    def reverseList(self):
        if self.start is None:
            return None

        if self.start.next is None:
            return self.start

        prevNode = self.start
        currNode = self.start.next

        prevNode.next = None
        while currNode.next is not None:
            temp = id(currNode.next)
            currNode.next = prevNode
            prevNode = currNode
            currNode = ctypes.cast(temp, ctypes.py_object).value

        self.start = currNode
        currNode.next = prevNode
        return self.start
    
def main():
    DLL = LinkedList()
    
    n1 = Node(1)
    DLL.insert_At_Last(n1)

    n2 = Node(2)
    DLL.insert_At_Last(n2)

    n3 = Node(3)
    DLL.insert_At_Last(n3)
    
    n4 = Node(4)
    DLL.insert_At_Last(n4)

    DLL.showLL()

    DLL.reverseList()

    print("REVERSE LINKED LIST")
    DLL.showLL()

if __name__ == "__main__":
    main()