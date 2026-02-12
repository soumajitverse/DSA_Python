class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLinkedlist:
    def __init__(self, head = None):
        self.head = head

    # method to insert a node at end
    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    # method to insert a node at beginning
    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    # method to insert a node just after a given value present in the singly LL
    def insertInMid(self, value, x):

        # if the list is empty
        if(self.head == None):
            print("List is empty")
            return

        temp = Node(value)
        t1 = self.head

        while(t1 != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
                return 
            t1 = t1.next
       
    # method to delete a node by a given value present in the singly LL
    def deleteLL(self, value):

        # empty list
        if(self.head == None):
            return

        # delete head
        if(self.head.data == value):
            self.head = self.head.next
            return
        
        # t1 = self.head
        # prev = t1

        prev = self.head
        t1 = prev.next

        while(t1 != None):
            if(t1.data == value):
                prev.next = t1.next
                return
            else:
                prev = t1
                t1 = t1.next

    # method to print the whole singly linked list
    def printLL(self):

        # if the list is empty
        if(self.head == None):
            print("List is empty")
            return
        
        t1 = self.head
        while(t1 != None):
            print(t1.data)
            t1 = t1.next

obj = SinglyLinkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(50)
obj.insertInMid(22, 20)
print("Before deletion")
obj.printLL()
obj.deleteLL(50)
print("After deletion")
obj.printLL()
