class Node:
    def __init__(self, value = None):
        self.data = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # insert at end
    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        t = self.head
        while(t.next != None):
            t = t.next
        t.next = temp
        temp.prev = t

    # insert at beginning 
    def insertAtBeg(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
    
    # insert a node just after a specific value
    def insertInMid(self, value, x):

        # if the list is empty
        if(self.head == None):
            print("List is empty")
            return
        
        temp = Node(value)
        t = self.head

        while(t != None):
            if(t.data == x):
                temp.prev = t
                temp.next = t.next

                # if x is at last
                if(t.next != None):
                    t.next.prev = temp

                t.next = temp
                return
            t = t.next                

    # delete a node by value
    def deleteDLL(self, value):
        # if the list is empty
        if(self.head == None):
            print("List is empty")
            return
        
        # if the value is at first node
        if(self.head.data == value):
            self.head = self.head.next
            # if there is a node present after the deleted node in the list
            if(self.head != None):
                self.head.prev = None
                return
            return
        

        t = self.head
        while(t != None):

            if(t.data == value):

                # if the value is present at last node
                if(t.next == None):
                    t.prev.next = None
                    return

                t.prev.next = t.next
                t.next.prev = t.prev
                return
            
            t = t.next
        
        print("Value not found")


    # print the DLL
    def printDLL(self):
        # if the list is empty
        if(self.head == None):
            print("List is empty")
            return
        
        t = self.head
        while(t.next != None):
            print(t.data, end=" <--> ")
            t = t.next
        print(t.data)


obj = DoublyLinkedList()
obj.insertAtEnd(2)
obj.insertAtEnd(5)
obj.insertAtEnd(18)
obj.insertAtEnd(6)
obj.insertAtEnd(9)
obj.insertAtBeg(7)
obj.insertInMid(50, 7)
print("Before deletion")
obj.printDLL()
obj.deleteDLL(2)
print("After deletion")
obj.printDLL()