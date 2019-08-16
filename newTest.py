import unittest
from lesson1_2 import Node
from lesson1_2 import LinkedList2
import random

class my_test:

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
        test.add_in_head(Node(777))
        test.print_all_nodes()
        print('test - ',test.head.value)

    def test3_add_in_head(self):
        test = LinkedList2()
        test.add_in_head(Node(1))
        print('test 1- ',test.head.value)
        test.add_in_head(Node(2))
        print('test 2- ',test.head.value)
        test.print_all_nodes()
        print('test321 - ',test.head.value,test.tail.value)

    def test4_add_in_head(self):
        test = LinkedList2()
        for i in range(10):
            test.add_in_head(Node(i))
        test.print_all_nodes()
        print('test321 - ',test.head.value,test.tail.value)

    def test1_clean(self):
        test = LinkedList2()
        for i in range(10):
            test.add_in_head(Node(i))
        test.print_all_nodes()
        test.clean()
        test.add_in_tail(Node(231))
        test.print_all_nodes()

    def test1_len(self):
        test = LinkedList2()
        for i in range(10):
            test.add_in_head(Node(i))
            print('leng - ', i,test.len())
        test.print_all_nodes()

    def test1_find(self):
        test = LinkedList2()
        for i in range(10):
            y = random.randint(0,10)
            test.add_in_tail(Node(y))
        test.print_all_nodes()
        for i in range(10):
            print('test - ',test.find(i),' value - ',i) 

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
        s_list.print_all_nodes()
        s_list.insert(Node(55),Node(66))
        print('_________________________')
        s_list.print_all_nodes()
        print('head - ',s_list.head.value,' tail - ', s_list.tail.value)

    def test12_insert(self):
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
        s_list.insert(Node(333),Node(66))
        print('_________________________')
        s_list.print_all_nodes()
        print('head - ',s_list.head.value,' tail - ', s_list.tail.value)

    def test13_insert(self):
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
        s_list.insert(Node(12),Node(66))
        print('_________________________')
        s_list.print_all_nodes()
        print('head - ',s_list.head.value,' tail - ', s_list.tail.value)

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
            test.print_all_nodes()
            print('__________')
            print("1head - ", test.head.value," 1tail - ", test.tail.value)
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
        test.print_all_nodes()
        print('______________________')
        test.insert(None,Node(90))
        test.print_all_nodes()
        print("head - ", test.head.value," tail - ", test.tail.value)

    def test4_insert(self):
        test = LinkedList2()
        v = "Вставка"
        print('______________________')
        test.insert(None,Node(v))
        test.print_all_nodes()
        print("head - ", test.head.value," tail - ", test.tail.value)

    def test1_del_false(self):
        test = LinkedList2()
        test.add_in_tail(Node(9))
        test.len()
        if(test.len() == 1):
            test.print_all_nodes()
            print('В спсике один элемент!')
        print('до удаления', test.head.value, test.tail.value, test.len())
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
        print('до удаления',s_list.head.value, s_list.tail.value, s_list.len())
        s_list.delete(333)
        print('после удаления',s_list.head.value, s_list.tail.value, s_list.len())
        print('___________')
        s_list.print_all_nodes()

    def test3_del_false(self):
        n1 = Node(12)
        n2 = Node(55)
        n1.next = n2 # 12 -> 55
        n2.prev = n1
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(333))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))
        s_list.print_all_nodes()
        print('до удаления',s_list.head.value, s_list.tail.value, s_list.len())
        s_list.delete(128)
        print('после удаления',s_list.head.value, s_list.tail.value, s_list.len())
        print('___________')
        s_list.print_all_nodes()


    def test1_del_true(self):
        test = LinkedList2()
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(0))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))
        test.print_all_nodes()
        print('до удаления', test.head.value, test.tail.value, test.len())
        test.delete(2, True)
        print('после удаления', test.head.value, test.tail.value, test.len())
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
        test.print_all_nodes()
        print('до удаления', test.head.value, test.tail.value, test.len())
        test.delete(2, True)
        print('после удаления', test.head.value, test.tail.value, test.len())
        len_2 = test.len()
        len_del = len_1 - len_2
        if(len_del == len_1 and test.head is None and test.len() == 0 and test.tail is None):
            print('Список пустой. Удаленно было ',len_del ,'элементов.')
        else:
            print('В списке осталось - ', len_2,'элементов.' , 'Удаленно было - ', len_del, 'элементов.')
            test.print_all_nodes()

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
            print(test.head.value, test.tail.value,' head - ',test.head.value,' tail - ',test.tail.value)        

test = my_test()
test.test4_del_true()