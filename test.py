import random 

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
                    break #до сюда вроде норм
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

class my_test:
    def test1_clean(self):
        n1 = Node(12)
        n2 = Node(55)
        n1.next = n2 # 12 -> 55
        n2.prev = n1
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(Node(128))
        s_list.clean()
        s_list.add_in_tail(Node(333))
        print('leng - ',s_list.len())
        s_list.print_all_nodes()

    def test2_clean(self):
        n1 = Node(12)
        n2 = Node(55)
        n1.next = n2 # 12 -> 55
        n2.prev = n1
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(333))
        print('leng - ',s_list.len())
        s_list.print_all_nodes()

    def test1_len(self):
        test = LinkedList2()
        for i in range(10):
            test.add_in_tail(Node(i))
            print('leng - ', i,test.len())
        test.print_all_nodes()

    def test1_find_all(self):
        test = LinkedList2()
        for i in range(10):
            y = random.randint(0,10)
            test.add_in_tail(Node(y))
        for j in range(10):
            y = random.randint(0,10)

    def test1_insert(self):
        n1 = Node(12)
        n2 = Node(55)
        n1.next = n2 # 12 -> 55
        n2.prev = n1
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(333))
        s_list.insert(55,66)
        s_list.print_all_nodes()

    def test2_insert(self):
        test = LinkedList2()
        v = "Вставка"
        for i in range(3):
            y = random.randint(0,10)
            test.add_in_tail(Node(y))
        for i in range(1):
            if(test.head is None and test.tail is None and test.len() == 0):
                print("Список пустой!")
            test.print_all_nodes()
            test.insert(test.head, Node(v))
            print("head - ", test.head.value," tail - ", test.tail.value)
            test.insert(test.tail, Node(v))
            print("head - ", test.head.value," tail - ", test.tail.value)
            test.print_all_nodes()

    def test3_insert(self):
        test = LinkedList2()
        v = "Вставка"
        for i in range(3):
            test.add_in_tail(Node(i))
        test.print_all_nodes()
        print('______________________')
        test.insert(None,Node(90))
        test.print_all_nodes()

    def test4_insert(self):
        test = LinkedList2()
        v = "Вставка"
        print('______________________')
        test.insert(None,Node(v))
        test.print_all_nodes()

    def test1_find(self):
        test = LinkedList2()
        for i in range(10):
            y = random.randint(0,10)
            test.add_in_tail(Node(y))
        test.print_all_nodes()
        for i in range(10):
            print('test - ',test.find(i),i) 

    def test1_find_all(self):
        test = LinkedList2()
        for i in range(10):
            y = random.randint(0,10)
            test.add_in_tail(Node(y))
        test.print_all_nodes()
        for i in range(10):
            print('test - ',test.find_all(i),i)

    def test1_add_in_head(self):
        test = LinkedList2()
        for i in range(10):
            y = random.randint(0,10)
            test.add_in_tail(Node(y))
        test.print_all_nodes()
        print('_______________________')
        test.add_in_head(Node('666'))
        test.print_all_nodes()

    def test2_add_in_head(self):
        test = LinkedList2()
        test.print_all_nodes()
        print('_______________________')
        test.add_in_head(Node('777'))
        test.print_all_nodes()
        print('test - ',test.head.value)

    def test1_del_false(self):
        test = LinkedList2()
        test.add_in_tail(Node(9))
        test.len()
        if(test.len() == 1):
            print('В спсике один элемент!')
            test.print_all_nodes()
        test.delete(9)
        print('после удаления', test.head, test.tail, test.len())
        if(test.head is None and test.tail is None and test.len() == 0):
            print('список пуст!')              

    def test2_del_false(self):
        n1 = Node(12)
        n2 = Node(55)
        n1.next = n2 # 12 -> 55
        n2.prev = n1
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(333))
        s_list.print_all_nodes()
        s_list.delete(333)
        print('___________')
        s_list.print_all_nodes()
        print(s_list.head.prev,s_list.tail.prev)


    def test1_del_true(self):
        test = LinkedList2()
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(0))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))
        test.delete(2, True)
        test.print_all_nodes()
        if(test.head is None and test.tail is None and test.len() == 0):
            print("Список пустой!")
        else:
            print('Список после удаления')
            test.print_all_nodes()
        
    def test2_del_true(self):
        test = LinkedList2()
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(6))
        test.add_in_tail(Node(2))
        len_1 = test.len()
        test.delete(2, True)
        len_2 = test.len()
        len_del = len_1 - len_2
        if(len_del == len_1 and test.head is None and test.len() == 0 and test.tail is None):
            print('Список пустой. Удаленно было ',len_del ,'элементов.')
        else:
            print('В списке осталось - ', len_2,'элементов.' , 'Удаленно было - ', len_del, 'элементов.')

    def test3_del_true(self):
        test = LinkedList2()
        test.add_in_tail(Node(0))
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))       
        y = 2
        test.print_all_nodes()
        len_1 = test.len()
        for i in range(test.len()):
            if(y == test.head.value and test.head.next is None):
                print('Удалятся будет последний узел')
        test.delete(y, True)
        len_2 = test.len()
        len_del = len_1 - len_2
        for i in range(test.len()):
            if (y != test.head.value):
                print('Удаление последнего узла прошло успешно!')
                break
        test.print_all_nodes()        
        print('Удаленно (',len_del,' элементов). Узла с значением -', y)

    def test4_del_true(self):
        test = LinkedList2()
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(3))
        test.add_in_tail(Node(3))
        test.add_in_tail(Node(3))
        test.add_in_tail(Node(3))
        len_1 = test.len()
        test.delete(3, True)
        len_2 = test.len()
        if (len_1 != len_2):
            print('Общее количество элементов до удаления - ', len_1, 'оставшееся количество элементов - ', len_2)
        if(test.len() == 2):
            print(test.head.value, test.tail.value)        
test = my_test()
test.test1_add_in_head()
test.test2_add_in_head()
test.test1_del_true()
print('+++++++++++++++')
test.test2_del_true()
print('+++++++++++++++')
test.test3_del_true()
print('+++++++++++++++')
test.test4_del_true()
print('===============')
test.test1_del_false()
print('++++++++++++++++')
test.test2_del_false()
print('++++++++++++++++')