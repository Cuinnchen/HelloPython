class Cat(object):

    def __init__(self):

        print("这是一个初始化犯法")
        # self.属性名 = 属性的初始值
        self.name = "Tom"

    def eat(self):

        print("%s 爱吃鱼" % self.name)
#  实例化时候，会自动调用初始化方法
tom = Cat()
tom.eat()
print(tom.name)
