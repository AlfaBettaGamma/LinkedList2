class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None
        self.leng = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, newNode):
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode
        pass # здесь будет ваш код


    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def clean(self):
        self.__init__()
        pass # здесь будет ваш код

    def len(self):
        self.leng = 0
        if(self.head is None):
            return self.leng
        node = self.head
        while node is not None:
            node = node.next
            self.leng +=1
        return self.leng # здесь будет ваш код 

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        list_val = []
        if(self.head == None):
            return list_val
        node = self.head
        while node is not None:
            if (node.value == val):
                list_val.append(node)
            node = node.next
        return list_val # здесь будет ваш код

    def insert(self, afterNode, newNode):
        node = self.head
        newN = newNode
        if afterNode is None and self.head == None:
            self.head = self.tail = newN
        elif afterNode is None:
            while node is not None:
                if node.next is None:
                    node.next = newN
                    newN.prev = node
                    newN.next = None
                    self.tail = newN
                node = node.next
        else:
            while node is not None:
                if(node.value == afterNode.value):
                    if node.next is None:
                        node.next = newN
                        newN.prev = node
                        newN.next = None
                        self.tail = newN
                    else:
                        newN.next = node.next
                        node.next.prev = newN
                        node.next = newN
                        newN.prev = node

                node = node.next
        pass # здесь будет ваш код

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = self.head.next
                    if self.head is not None:
                        self.head.prev = None
                if node == self.tail:
                    self.tail = node.prev
                    if self.tail is not None:
                        self.tail.next = None
                if node.prev is not None:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                node = node.next
                if not all:
                    return
            else:
                node = node.next
            pass