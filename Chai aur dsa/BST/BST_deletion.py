class Node:
    def __init__(self, value):
        self.left = self.right = None
        self.data = value

def insert(root, value):
    if(root == None):
        return Node(value)
    
    if(root.data == value):
        return root
    
    if(root.data > value):
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    return root

def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


# this is will return the inorder successor
def get_successor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root


def delete(root, value):
    if(root == None):
        return root
    
    elif(root.data > value):
        root.left = delete(root.left, value)
    
    elif(root.data < value):
        root.right = delete(root.right, value)
    
    else:

        # these two cases are for 1.deletion of leaf node (node with child), 2.deletion of node having one child
        
        # if the node has no left child then its right child will be transfered to the right of its parent 
        if(root.left == None):
            return root.right
        
        # if the node has no right child then its left child will be transfered to the left of its parent 
        if(root.right == None):
            return root.left
        
        # this is the case 3 where node has both left and right child
        else:
            succ = get_successor(root)
            root.data = succ.data # here we copy the value of succ.data to the root.data
            
            # and after that we will delete the successor
            root.right = delete(root.right, succ.data)

    return root
        

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)

inOrder(root)

# root = delete(root,12)
# root = delete(root,40)
root = delete(root,30)

print("\n")
inOrder(root)
