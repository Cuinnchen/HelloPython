class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1,self.__num2))

    def test(self):
        print("父类的公共方法 %d" % self.__num2)

        self.__test()

class B(A):

    def demo(self):
        # 1.在子类的对象方法中，不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        # 2.在子类的对象方法中不能，访问父类的私有方法
        # self.__test()

        # 3.F访问父类的公有方法
        self.test()
        print("子类方法%d " % self.num1)
        pass
# 创建一个子类对象
b = B()
print(b)
print()

# 在外界访问父类的公有属性和方法
# print(b.num1)
# # b.test()
b.demo()