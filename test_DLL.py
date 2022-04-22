from unittest import TestCase
from DLL import DoubleLL


class TestDoubleLinkedList(TestCase):
    def setUp(self):
        self.DLL = DoubleLL()

    def test_first_push(self):
        self.DLL.first_push(4)
        self.assertEqual(self.DLL.head.data, 4)

    def test_push_front(self):
        self.DLL.first_push(4)
        self.DLL.push_front(8)
        self.assertEqual(self.DLL.head.data, 8)
        self.assertEqual(self.DLL.head.next.data, 4)

    def test_push_end(self):
        self.DLL.first_push(4)
        self.DLL.push_end(9)
        self.assertEqual(self.DLL.head.data, 4)
        self.assertEqual(self.DLL.head.next.data, 9)

    def test_push_after(self):
        self.DLL.first_push(10)
        self.DLL.insert_after(10, 38)
        self.assertEqual(self.DLL.head.data, 10)
        self.assertEqual(self.DLL.head.next.data, 38)

    def test_push_before(self):
        self.DLL.first_push(55)
        self.DLL.insert_after(55, 29)
        self.DLL.insert_before(29, 100)
        self.assertEqual(self.DLL.head.data, 55)
        self.assertEqual(self.DLL.head.next.data, 100)
        self.assertEqual(self.DLL.head.next.next.data, 29)

    def test_delete_end(self):
        self.DLL.first_push(1)
        self.DLL.push_end(2)
        self.DLL.push_end(3)
        self.DLL.delete_end()
        self.assertEqual(self.DLL.head.data, 1)
        self.assertEqual(self.DLL.head.next.data, 2)

    def test_delete_by_value(self):
        self.DLL.first_push(10)
        self.DLL.push_end(20)
        self.DLL.push_end(30)
        self.DLL.delete_by_value(20)
        self.assertEqual(self.DLL.head.data, 10)
        self.assertEqual(self.DLL.head.next.data, 30)

    def test_reverse(self):
        self.DLL.first_push(10)
        self.DLL.push_end(20)
        self.DLL.insert_before(20, 40)
        self.DLL.reverse_list()
        self.assertEqual(self.DLL.head, self.DLL.head)
