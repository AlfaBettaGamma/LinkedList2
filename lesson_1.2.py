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
    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
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

    def delete(self, val, all=False):
        leng = 0
        if(self.head is None):
            return print("список пуст")
        node = self.head   
        if(all is False):  
            while node != None:
                if(leng == 0 and node.value == val):
                    if(node.next is None):
                        self.head = None
                        self.tail = None
                    self.head = node.next
                    leng += 1
                    break 
                if(node.next != None):
                    if(node.next.value == val):
                        node.next = node.next.next     
                        if(node.next is None):
                            node = None
                            if(self.head is None and leng == 0):
                                self.tail = None
                            self.tail = self.head.next
                        else:
                            node.next.prev = node.next 
                        break
                    node = node.next
                else:
                    self.head = None
                    self.tail = None
        elif(all is True):
            while node != None:
                if(node.next != None):
                    if(leng == 0 and node.value is val):
                        node = node.next
                    elif(node.next.value is val):
                        node.next = node.next.next
                        if(node.next is None):
                            node = None
                            self.tail = self.head.next
                        else:
                            node.next.prev = node.next 
                    else:
                        node = node.next
                        leng += 1
                else:
                    if(node.value == val):
                        self.head = None
                        self.tail = None
                    break
            pass # здесь будет ваш код

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

    def insert(self, afterNode, newNode):
        node = self.head
        newN = newNode
        if afterNode == None and self.head == None:
            self.head = self.tail = newNode
        elif afterNode is None:
            while node is not None:
                if node.next is None:
                    node.next = newN
                    newN.prev = node
                    newN.next = None
                node = node.next
        else:
            while node is not None:
                if(node.value == afterNode.value):
                    if node.next is None:
                        node.next = newN
                        newN.prev = node
                        newN.next = None
                    else:
                        newN.next = node.next
                        node.next.prev = newN
                        node.next = newN
                        newN.prev = node
                if(newN.next is None):
                    self.tail = newN
                node = node.next
        pass # здесь будет ваш код

    def add_in_head(self, newNode):
        if self.head == None:
            self.head = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
        pass # здесь будет ваш код  