import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox
from facade import Facade
import logging

logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    def __init__(self, facade):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi('forms/MainWindow.ui', self)
        self.facade = facade
        self.list = []
        self.string = '123'
        self.btn_push_first.clicked.connect(lambda: self.push_first())
        self.btn_push_front.clicked.connect(lambda: self.push_front())
        self.btn_push_end.clicked.connect(lambda: self.push_end())
        self.btn_push_after.clicked.connect(lambda: self.push_after())
        self.btn_push_before.clicked.connect(lambda: self.push_before())
        self.btn_del_first.clicked.connect(lambda: self.delete_first())
        self.btn_del_end.clicked.connect(lambda: self.delete_end())
        self.btn_del_value.clicked.connect(lambda: self.delete_value())
        self.btn_del_all.clicked.connect(lambda: self.delete_all())
        self.btn_reverse.clicked.connect(lambda: self.reverse())
        self.btn_save.clicked.connect(lambda: self.save())
        self.btn_load.clicked.connect(lambda: self.load())

        self.build()

    def push_first(self):
        self.ui = PushFirst(self.facade, self)
        self.ui.show()

    def push_front(self):
        self.ui = PushFront(self.facade, self)
        self.ui.show()

    def push_end(self):
        self.ui = PushEnd(self.facade, self)
        self.ui.show()

    def push_after(self):
        self.ui = PushAfter(self.facade, self)
        self.ui.show()

    def push_before(self):
        self.ui = PushBefore(self.facade, self)
        self.ui.show()

    def delete_first(self):
        self.facade.delete_first()
        self.build()

    def delete_end(self):
        self.facade.delete_end()
        self.build()

    def delete_all(self):
        self.facade.delete_all()
        self.build()

    def delete_value(self):
        self.ui = DeleteValue(self.facade, self)
        self.ui.show()

    def reverse(self):
        self.facade.reverse_list()
        self.build()

    def save(self):
        if self.list == ['[]']:
            logging.log(logging.INFO, 'Список пустой!')
        else:
            self.facade.save_db()
            print('saved')

    def load(self):
        self.list = self.facade.load()
        if self.list is not None and self.list != []:
            self.build()
            logging.log(logging.INFO, 'Загружено!')
        else:
            logging.log(logging.INFO, 'В базе данных ничего нет!')

    def build(self):
        self.list = self.facade.get()
        self.listWidget.clear()

        if (type(self.list)) == (type(self.string)):
            self.list = [self.list]

        if self.list is not None:
            self.listWidget.clear()
            self.listWidget.addItems(self.list)


class PushFirst(QWidget):
    def __init__(self, facade, link=None):
        self.facade = facade
        self.link = link
        super(PushFirst, self).__init__()
        self.ui = uic.loadUi('forms/pushFirst.ui', self)
        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.data = self.lineEdit.text()
        if self.data == '':
            self.warning_no_nums()
        elif self.data.isnumeric() is False:
            self.warning_no_int()
        else:
            self.data = int(self.data)
            self.facade.push_first(self.data)
            self.link.build()

    def warning_no_int(self):
        """
        Создание MessageBox, если данные содержат буквы и символы.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Введите число!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()

    def warning_no_nums(self):
        """
        Создание MessageBox, если данные не введены.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Заполните поле!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()


class PushFront(QWidget):
    def __init__(self, facade, link=None):
        self.facade = facade
        self.link = link
        super(PushFront, self).__init__()
        self.ui = uic.loadUi('forms/pushFront.ui', self)
        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.data = self.lineEdit.text()
        if self.data == '':
            self.warning_no_nums()
        elif self.data.isnumeric() is False:
            self.warning_no_int()
        else:
            self.data = int(self.data)
            self.facade.push_front(self.data)
            self.link.build()

    def warning_no_int(self):
        """
        Создание MessageBox, если данные содержат буквы и символы.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Введите число!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()

    def warning_no_nums(self):
        """
        Создание MessageBox, если данные не введены.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Заполните поле!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()



class PushEnd(QWidget):
    def __init__(self, facade, link=None):
        self.facade = facade
        self.link = link
        super(PushEnd, self).__init__()
        self.ui = uic.loadUi('forms/pushEnd.ui', self)
        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.data = self.lineEdit.text()
        if self.data == '':
            self.warning_no_nums()
        elif self.data.isnumeric() is False:
            self.warning_no_int()
        else:
            self.data = int(self.data)
            self.facade.push_end(self.data)
            self.link.build()

    def warning_no_int(self):
        """
        Создание MessageBox, если данные содержат буквы и символы.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Введите число!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()

    def warning_no_nums(self):
        """
        Создание MessageBox, если данные не введены.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Заполните поле!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()


class PushAfter(QWidget):
    def __init__(self, facade, link=None):
        self.facade = facade
        self.link = link
        super(PushAfter, self).__init__()
        self.ui = uic.loadUi('forms/pushAfter.ui', self)
        self.pushButton.clicked.connect(self.push_after)

    def push_after(self):
        self.current = self.lineEdit.text()
        self.data = self.lineEdit_2.text()

        if self.current == '':
            self.warning_no_nums()
        elif self.data == '':
            self.warning_no_nums()
        elif self.current.isnumeric() is False:
            self.warning_no_int()
        elif self.data.isnumeric() is False:
            self.warning_no_int()
        else:
            self.current = int(self.current)
            self.data = int(self.data)
            self.facade.insert_after(self.current, self.data)
            self.link.build()

    def warning_no_int(self):
        """
        Создание MessageBox, если данные содержат буквы и символы.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Введите число!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()

    def warning_no_nums(self):
        """
        Создание MessageBox, если данные не введены.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Заполните поле!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()


class PushBefore(QWidget):
    def __init__(self, facade, link=None):
        self.facade = facade
        self.link = link
        super(PushBefore, self).__init__()
        self.ui = uic.loadUi('forms/pushBefore.ui', self)
        self.pushButton.clicked.connect(self.push_before)

    def push_before(self):
        self.current = self.lineEdit.text()
        self.data = self.lineEdit_2.text()

        if self.current == '':
            self.warning_no_nums()
        elif self.data == '':
            self.warning_no_nums()
        elif self.current.isnumeric() is False:
            self.warning_no_int()
        elif self.data.isnumeric() is False:
            self.warning_no_int()
        else:
            self.current = int(self.current)
            self.data = int(self.data)
            self.facade.insert_before(self.current, self.data)
            self.link.build()

    def warning_no_int(self):
        """
        Создание MessageBox, если данные содержат буквы и символы.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Введите число!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()

    def warning_no_nums(self):
        """
        Создание MessageBox, если данные не введены.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Заполните поле!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()


class DeleteValue(QWidget):
    def __init__(self, facade, link=None):
        self.facade = facade
        self.link = link
        super(DeleteValue, self).__init__()
        self.ui = uic.loadUi('forms/delete.ui', self)
        self.pushButton.clicked.connect(self.delete_value)

    def delete_value(self):
        self.data = self.lineEdit.text()
        if self.data == '':
            self.warning_no_nums()
        elif self.data.isnumeric() is False:
            self.warning_no_int()
        else:
            self.data = int(self.data)
            self.facade.delete_by_value(self.data)
            self.link.build()

    def warning_no_int(self):
        """
        Создание MessageBox, если данные содержат буквы и символы.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Введите число!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()

    def warning_no_nums(self):
        """
        Создание MessageBox, если данные не введены.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Заполните поле!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()



class Builder:
    def __init__(self):
        self.facade = None
        self.gui = None

    def create_facade(self):
        self.facade = Facade()

    def create_gui(self):
        if self.facade is not None:
            self.gui = MainWindow(self.facade)

    def get_result(self):
        if self.facade is not None and self.gui is not None:
            return self.gui


if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    builder = Builder()
    builder.create_facade()
    builder.create_gui()
    window = builder.get_result()
    window.show()
    qapp.exec()
