class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")

class Dog(Animal):

    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("汪汪叫")

class Xiaotianquan(Dog):
    def fly(self):
        print("我会飞")

class Cat(Animal):
    def catch(self):
        print("抓老鼠")

xtq = Xiaotianquan()
xtq.fly()
xtq.run()
