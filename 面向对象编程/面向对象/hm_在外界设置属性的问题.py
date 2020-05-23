class Cat(object):
    # def __init__(self):
    #     self.name = "tom"

    def eat(self):
        print("%s 爱吃鱼"% self.name)

    def drink(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱喝水"% self.name)


tom = Cat()


# 可以使用 .属性名 利用赋值语句就可以
# tom.name = "Tom"
tom.drink()
tom.eat()
tom.name = "Tom"