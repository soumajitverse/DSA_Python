class Stack:
    def __init__(self):
        self.s = []

    def push(self, value):
        # self.s.insert(0, value) # it will take O(n) time complexity
        self.s.append(value) # this will take O(1)

    def pop(self):
        if not self.s:
            raise IndexError("Stack is empty")
        return self.s.pop()

    def peek(self):
        if not self.s:
            raise IndexError("Stack is empty")
        return self.s[-1]

    def is_empty(self):
        return not self.s

    def length(self):
        return len(self.s)


stk = Stack()

try:
    # stk.pop()
    stk.push(10)
    stk.push(20)
    stk.push(30)
    stk.push(40)
    print(stk.peek())
    print(stk.pop())
    print(stk.peek())

except Exception as e:
    print(e)

