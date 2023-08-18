# Add node at start
class node:
    def __init__(self, data) -> None:
        self.data: int = data   # this means node will hold integer value only
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertAtStart(self, data: int):
        n0 = node(data)
        n1 = self.head    
        
        n1.prev = n0

        n0.next = n1
        n0.prev = None

        self.head = n0

    def showDLL(self):
        printVal = self.head
        while printVal is not None:
            print(printVal.data, end=" ")
            printVal = printVal.next
    

def main():
    DLL = DLinkedList()
    
    n1 = node(1)  
    n2 = node(2)
    n3 = node(3)
    
    DLL.head = n1
    n1.next = n2
    n1.prev = None

    n2.next = n3
    n2.prev = n1

    n3.next = None
    n3.prev = n2 

    DLL.showDLL()

    #Insert Here
    data = int(input("Enter Value to Insert at first"))
    DLL.insertAtStart(data)

    DLL.showDLL()


if __name__ == "__main__":
    main()