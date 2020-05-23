class A:

    def test(self):
        print("test方法")


class B:

    def demo(self):
        print("demo 方法")


class C(A,B):
    """多继承可以让子类对象，同事具有多个父类的属性和方法"""
    pass

# 创建子类对象

c = C()

c.test()
c.demo()