class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end =' -> ')
            temp = temp.next
    
    def append(self, value):
        # Edge cases: 
        # a) when Node == None
        new_node = Node(value)
        #print(self.head.value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # Links new node to the LL
            self.tail = new_node # Tail pointer shift to new node
        self.length += 1
        return True
        
    def pop(self):
        # Edge cases: 
        # a) when Node == None
        if self.length == 0:
            return None
        
        # c) when self.length is >= 1
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        # b) when self.length == 1 (after popping self.length = 0)
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp
        
    def prepend(self, value):
        # Edge cases: 
        # a) when Node == None
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True
        
        
        
        
        

''' #Initialise and test check 
my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
'''

my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.pop()
my_linked_list.prepend(2)
my_linked_list.print_list()


                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
