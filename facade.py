from DLL import DoubleLL
from DLL_DB import Database


class Facade:
    def __init__(self, name='DLL_DB.db'):
        self.DLL = DoubleLL()
        self.DB = Database(name)

    def push_first(self, data):
        self.DLL.first_push(data)
        self.save_list()

    def push_front(self, data):
        self.DLL.push_front(data)
        self.save_list()

    def push_end(self, data):
        self.DLL.push_end(data)
        self.save_list()

    def insert_after(self, current, data):
        self.DLL.insert_after(current, data)
        self.save_list()

    def insert_before(self, current, data):
        self.DLL.insert_before(current, data)
        self.save_list()

    def delete_by_value(self, data):
        self.DLL.delete_by_value(data)
        self.save_list()

    def delete_first(self):
        self.DLL.delete_first()
        self.save_list()

    def delete_end(self):
        self.DLL.delete_end()
        self.save_list()

    def delete_all(self):
        self.DLL.delete_all()
        self.DB.delete_all()
        self.save_list()

    def reverse_list(self):
        self.DLL.reverse_list()
        self.save_list()

    def save_list(self):
        self.DLL.save_list()

    def save_db(self):
        elem = self.DLL.save_list()
        self.DB.add_values(elem)

    def get(self):
        self.data = self.DLL.save_list()
        print(self.data)
        return self.data

    def load(self):
        load = []
        if self.DB.load_last() is not None:
            nums = self.DB.load_last()[0][1:-1].split(',')
            if nums != ['']:
                for num in nums:
                    load.append(int(num))
                    self.DLL.delete_all()

        for i in load:
            self.push_end(i)

        return load
