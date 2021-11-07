from collections import Iterable
from collections import Iterator
import time
class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，既可以使用for，那么必须实现__iter__方法"""
        return ClassIterator(self)

class ClassIterator():

    def __init__(self,obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise  StopIteration



classmata = Classmate()

classmata.add('老王')
classmata.add('李四')
classmata.add('王二')
# print(classmata.names)
# classmata.add('张三')

# print(isinstance(classmata,Iterable))  # 判断是否可迭代
# classmate_iterator = iter(classmata)
# print(isinstance(classmate_iterator,Iterator))  # 判断是否迭代器
# iter(classmata)

# print(next(classmate_iterator))
for name in classmata:
    print(name)
    time.sleep(1)
"""
for循环：

1.判断xxx是否是可以迭代
2.在第一步成立的前提下，调用iter函数
得到xxx对象的__iter__方法的返回值
3.__iter__方法的返回值是一个迭代器
"""