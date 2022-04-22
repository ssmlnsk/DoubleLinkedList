import json


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLL:
    def __init__(self):
        self.head = None

    def first_push(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("List isn't empty")

    def push_front(self, data):
        if self.head is None:
            self.first_push(data)
            return
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_end(self, data):
        if self.head is None:
            self.first_push(data)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        new_node = Node(data)
        node.next = new_node
        new_node.prev = node

    def insert_after(self, current, data):
        if self.head is None:
            print("list is empty")
            return
        else:
            node = self.head
            while node is not None:
                if node.data == current:
                    break
                node = node.next
            if node is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.prev = node
                new_node.next = node.next
                if node.next is not None:
                    node.next.prev = new_node
                node.next = new_node

    def insert_before(self, current, data):
        if self.head is None:
            print("list is empty")
            return
        else:
            node = self.head
            while node is not None:
                if node.data == current:
                    break
                node = node.next
            if node is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.next = node
                new_node.prev = node.prev
                if node.prev is not None:
                    node.prev.next = new_node
                node.prev = new_node

    def delete_by_value(self, data):
        if self.head is None:
            print("list is empty already")
            return

        if self.head.next is None:
            if self.head.data == data:
                self.head = None
            else:
                print("item isn`t found")
            return

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        node = self.head
        while node.next is not None:
            if node.data == data:
                break
            node = node.next
        if node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            print("element isn`t found")

    def delete_first(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("list is empty")
            return
        elif self.head.next is None:
            self.head = None
            return
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.prev.next = None

    def delete_all(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            node = self.head
            while node is not None:
                self.delete_first()
                node = node.next

    def reverse_list(self):
        if self.head is None:
            print("list is empty")
            return
        temp = self.head
        next = temp.next
        temp.next = None
        temp.prev = next
        while next is not None:
            next.prev = next.next
            next.next = temp
            temp = next
            next = next.prev
        self.head = temp

    def save_list(self):
        self.list = []
        node = self.head
        while node is not None:
            self.list.append(node.data)
            node = node.next
        self.json = json.dumps(self.list)
        return self.json
