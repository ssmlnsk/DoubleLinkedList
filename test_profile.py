from random import randint

from DLL import DoubleLL

DLL = DoubleLL()

pfirst = randint(0, 100)
DLL.first_push(pfirst)

i_pushend = randint(0, 100)

for j_pushend in range(10000):
    DLL.push_end(i_pushend)

for j_pushfront in range(10000):
    i_pushfront = randint(0, 100)
    DLL.push_front(i_pushfront)

for j in range(10000):
    i = randint(0, 100)
    DLL.insert_after(pfirst, i)

for x in range(10000):
    i = randint(0, 100)
    DLL.insert_before(i_pushend, i)

DLL.delete_first()

DLL.delete_end()

DLL.push_end(3)

DLL.delete_by_value(3)

DLL.reverse_list()

DLL.save_list()
