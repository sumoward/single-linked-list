"""
Brian Ward
25/06/2014
Implementation of Single_Linked_List with recursive and iterative reversal

Using any programming language you're comfortable with,
write the required class(es) to implement
a simple singly-linked list.

Write two functions to
reverse the order of a singly-linked list using your implementation.
You must provide:
1. An iterative reverse.
2. A recursive reverse.
3. A full suite of automated tests.

"""


class Single_Linked_List():

    #private class for nodes of linked list
    class __SLLNode():

        def __init__(self, store, next_node):
            self.store = store
            self.next = next_node

        def __str__(self):
            return str(self.store)

#constructor
    def __init__(self):
        self.head = None
        self.tail = None
        # saves us iterating over the list each time we want length, O(1)
        self.length = 0

#returns the length of the list
    def __len__(self):
        return self.length

#__str__ over the list
    def __str__(self):
        node = self.head
        output = '['
        while node is not None:
            store = node.store
            try:
                store = str(store)
            except ValueError:
                store = store
            output = output + ' ' + store
            node = node.next
        return (output + ' ]')

#check whether the list is empty
    def isEmpty(self):
        return self.length == 0

#to add a new node after an existing node
    def insert_node(self,  store, node):
        new_node = Single_Linked_List.__SLLNode(store, node.next)
        node.next = new_node
        if self.tail == node:
            self.tail = new_node
        self.length = self.length + 1
        #print('self.length  insert', self.length)
        return new_node

#add a node at the start of the list
    def insert_start_of_list(self, store):
        new_node = Single_Linked_List.__SLLNode(store, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        #print('self.head', self.head)
        self.length = self.length + 1
        #print('self.length start', self.length)
        return new_node

#add a node at the end of the list
    def insert_end_of_list(self, store):
        if self.tail is None:
            new_node = Single_Linked_List.__SLLNode(store, None)
            self.tail = new_node
            if self.head is None:
                self.head = self.tail
            self.length = self.length + 1
        else:
            new_node = self.insert_node(store, self.tail)
        return new_node

#remove a node that follows a particular node from the list
    def remove_following_node(self, node):
        if node.next is None:
            self.tail = node
            self.length = self.length - 1
            return
        node.next = node.next.next
        self.length = self.length - 1

#remove a node from the beginning of a list
    def remove_start_of_list(self):
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length = self.length - 1

#iterative solution to reversal of the list, it uses 3 'pointers'
    def reverse_list_iterative(self):
        if self.head == 0 or self.tail == 0:
            return
        pointera = self.head
        pointerb = pointera.next
        pointerc = pointerb.next
        pointera.next = None
        pointerb.next = pointera
        pointera = pointerb
        while pointerc != None:
            pointerb = pointerc
            pointerc = pointerc.next
            pointerb.next = pointera
            pointera = pointerb
        self.head = pointerb

#calls recursive solution to reversal of the list on the start of a list
    def recursive_algo(self):
        self._recursive_algo(self.head)

#recursive solution
    def _recursive_algo(self, node):
        if node != None:
            right = node.next
            if node != self.head:
                node.next = self.head
                self.head = node
            else:
                node.next = None
            self._recursive_algo(right)

#find the node with a given value stored in it
    def find_value(self, value):
        node = self.head
        while node is not None:
            if node.store == value:
                return node
            node = node.next
        return node
