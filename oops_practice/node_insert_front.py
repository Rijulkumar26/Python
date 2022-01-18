class node():
    def __init__(self,node_data):
        self.data = node_data
        self.next = None
        
class linkedlist():
    def __init__(self):
        self.head = None
    
    def insert_at_front(self,new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printllist(self):
        if self.head is None:
            print('list is empty')
            return
        
        temp = self.head
        while(temp):
            print(str(temp.data) + ' ---->',end=' ')
            temp = temp.next

llist = linkedlist()
llist.insert_at_front('appy')
llist.insert_at_front('coke')
llist.insert_at_front('fanta')
llist.printllist()