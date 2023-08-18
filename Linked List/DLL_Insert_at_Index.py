# Methods Implemented Below
# 1. Insert At Last, Insert At Tails
# 1. Insert After Given Node
class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.next = None
        self.data = data

class DLL_Insert_At_Index():
    def __init__(self) -> None:
        self.start = None

    def showDLL(self):
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
            Node.prev = None
            return
        
        currNode = self.start
        while currNode.next is not None:
            currNode = currNode.next

        currNode.next = Node
        Node.prev = currNode
    
    def insert_After_Node(self, Node: Node, prevNode: Node):
        Node.prev = prevNode
        Node.next = prevNode.next

        prevNode.next = Node

        if Node.next is not None:
            Node.next.prev = Node

def main():
    DLL = DLL_Insert_At_Index()
    
    n1 = Node(1)
    DLL.insert_At_Last(n1)

    n2 = Node(2)
    DLL.insert_At_Last(n2)

    n3 = Node(3)
    DLL.insert_At_Last(n3)

    DLL.showDLL()

    n0 = Node(0)
    DLL.insert_After_Node(n0, n1)

    n0 = Node(0)
    DLL.insert_After_Node(n0, n1)

    DLL.showDLL()

    n4 = Node(4)
    DLL.insert_At_Last(n4)

    DLL.showDLL()

if __name__ == "__main__":
    main()