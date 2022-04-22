import sys
from unittest import TestCase

from PyQt5 import QtCore
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from GUI import MainWindow, PushFront, PushAfter, PushEnd, PushBefore, PushFirst, DeleteValue
from facade import Facade


class FunctionalTest(TestCase):
    def setUp(self):
        self.qapp = QApplication(sys.argv)
        name = 'test.db'
        self.facade = Facade(name)
        self.window = MainWindow(self.facade)

    def test1_push_first(self):
        btn_push_first = self.window.ui.btn_push_first
        QTest.mouseClick(btn_push_first, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushFirst):
                dialog = window
                break

        dialog.lineEdit.setText("")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("a")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("1")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("2")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test2_push_end(self):
        btn_push_end = self.window.ui.btn_push_end
        QTest.mouseClick(btn_push_end, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushEnd):
                dialog = window
                break

        self.facade.push_first(1)

        dialog.lineEdit.setText("4")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("5")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("6")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("a")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test3_push_front(self):
        btn_push_front = self.window.ui.btn_push_front
        QTest.mouseClick(btn_push_front, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushFront):
                dialog = window
                break

        dialog.lineEdit.setText("10")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("a")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("10")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("20")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("40")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test4_insert_before(self):
        btn_push_before = self.window.ui.btn_push_before
        QTest.mouseClick(btn_push_before, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushBefore):
                dialog = window
                break

        dialog.lineEdit.setText("1")
        dialog.lineEdit_2.setText("2")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        self.facade.push_first(1)
        self.facade.push_end(5)
        self.facade.push_end(9)

        dialog.lineEdit.setText("5")
        dialog.lineEdit_2.setText("8")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("9")
        dialog.lineEdit_2.setText("20")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("0")
        dialog.lineEdit_2.setText("50")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("")
        dialog.lineEdit_2.setText("")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("5")
        dialog.lineEdit_2.setText("")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("a")
        dialog.lineEdit_2.setText("b")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("5")
        dialog.lineEdit_2.setText("b")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test5_insert_after(self):
        btn_push_after = self.window.ui.btn_push_after
        QTest.mouseClick(btn_push_after, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushAfter):
                dialog = window
                break

        dialog.lineEdit.setText("1")
        dialog.lineEdit_2.setText("2")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        self.facade.push_first(1)
        self.facade.push_end(5)
        self.facade.push_end(9)

        dialog.lineEdit.setText("5")
        dialog.lineEdit_2.setText("10")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("9")
        dialog.lineEdit_2.setText("50")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("0")
        dialog.lineEdit_2.setText("70")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("")
        dialog.lineEdit_2.setText("")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("1")
        dialog.lineEdit_2.setText("")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("a")
        dialog.lineEdit_2.setText("b")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("1")
        dialog.lineEdit_2.setText("b")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test6_del_first(self):
        btn_del_first = self.window.ui.btn_del_first
        QTest.mouseClick(btn_del_first, QtCore.Qt.MouseButton.LeftButton)

        self.facade.push_first(4)
        self.facade.push_end(8)

        btn_del_first = self.window.ui.btn_del_first
        QTest.mouseClick(btn_del_first, QtCore.Qt.MouseButton.LeftButton)

        btn_del_first = self.window.ui.btn_del_first
        QTest.mouseClick(btn_del_first, QtCore.Qt.MouseButton.LeftButton)

    def test7_del_end(self):
        btn_del_end = self.window.ui.btn_del_end
        QTest.mouseClick(btn_del_end, QtCore.Qt.MouseButton.LeftButton)

        self.facade.push_first(10)
        self.facade.push_end(15)
        self.facade.push_end(20)

        btn_del_end = self.window.ui.btn_del_end
        QTest.mouseClick(btn_del_end, QtCore.Qt.MouseButton.LeftButton)

        btn_del_end = self.window.ui.btn_del_end
        QTest.mouseClick(btn_del_end, QtCore.Qt.MouseButton.LeftButton)

        btn_del_end = self.window.ui.btn_del_end
        QTest.mouseClick(btn_del_end, QtCore.Qt.MouseButton.LeftButton)

    def test8_del_by_value(self):
        btn_del_value = self.window.ui.btn_del_value
        QTest.mouseClick(btn_del_value, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, DeleteValue):
                dialog = window
                break

        dialog.lineEdit.setText("1")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        self.facade.push_first(10)

        dialog.lineEdit.setText("50")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("10")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        self.facade.push_first(30)
        self.facade.push_end(60)
        self.facade.push_end(40)

        dialog.lineEdit.setText("50")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("30")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("a")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test9_reverse(self):
        btn_reverse = self.window.ui.btn_reverse
        QTest.mouseClick(btn_reverse, QtCore.Qt.MouseButton.LeftButton)

        self.facade.push_first(10)
        self.facade.push_end(15)
        self.facade.push_end(20)
        self.facade.insert_before(15, 13)

        btn_reverse = self.window.ui.btn_reverse
        QTest.mouseClick(btn_reverse, QtCore.Qt.MouseButton.LeftButton)

    def test10_delete(self):
        btn_del_all = self.window.ui.btn_del_all
        QTest.mouseClick(btn_del_all, QtCore.Qt.MouseButton.LeftButton)

        self.facade.push_first(10)
        self.facade.push_end(20)
        self.facade.push_end(30)

        btn_del_all = self.window.ui.btn_del_all
        QTest.mouseClick(btn_del_all, QtCore.Qt.MouseButton.LeftButton)

        self.facade.delete_all()

    def test11_save(self):
        btn_save = self.window.ui.btn_save
        QTest.mouseClick(btn_save, QtCore.Qt.MouseButton.LeftButton)

        btn_push_end = self.window.ui.btn_push_end
        QTest.mouseClick(btn_push_end, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushEnd):
                dialog = window
                break

        dialog.lineEdit.setText("1")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)
        dialog.lineEdit.setText("2")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)
        dialog.lineEdit.setText("3")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        QTest.mouseClick(btn_save, QtCore.Qt.MouseButton.LeftButton)

    def test12_load(self):
        self.facade.delete_all()
        btn_load = self.window.ui.btn_load
        btn_save = self.window.ui.btn_save
        QTest.mouseClick(btn_load, QtCore.Qt.MouseButton.LeftButton)

        btn_push_end = self.window.ui.btn_push_end
        QTest.mouseClick(btn_push_end, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushEnd):
                dialog = window
                break

        dialog.lineEdit.setText("1")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)
        dialog.lineEdit.setText("2")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        QTest.mouseClick(btn_save, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("3")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        QTest.mouseClick(btn_load, QtCore.Qt.MouseButton.LeftButton)
