class Stack:
    def __init__(self):
        self.s = [] # empty list

    # it will return the no. of element present in the stack
    def length(self):
        return len(self.s)
    
    # it will insert the element at index = 0
    def push(self, value):
        self.s.insert(0, value)

    # it will show the top element means the 0 index element
    def peek(self):
       if self.length() == 0:
           raise Exception("Stack is Empty")
       else:
           return self.s[0]
       
    # it will delete the top most element means the 0 index element
    def pop(self):
       if self.length() == 0:
           raise Exception("Stack is Empty")
       else:
           return self.s.pop(0)


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


      