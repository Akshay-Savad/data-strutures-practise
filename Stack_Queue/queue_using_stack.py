import queue
class MyQueue:
    def __init__(self):
        self.st = []    
        self.st2 = []    

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        while self.st:
            temp = self.st.pop()
            self.st2.append(temp)

        result = self.st2.pop()
        while self.st2:
            temp = self.st2.pop()
            self.st.append(temp)

        return result

    def peek(self) -> int:
        return self.st[0]

    def empty(self) -> bool:
        return False if len(self.st) > 0 else True


# Your MyStack object will be instantiated and called as such:
def main():
    obj = MyQueue()
    # obj.push("1")
    # obj.push("2")
    # param_2 = obj.pop()
    # param_3 = obj.peek()
    param_4 = obj.empty()
    print(param_4)

if __name__ == "__main__":
    main()