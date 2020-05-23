class Cat(object):

    def __init__(self,new_name):

        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)

# TOM是一个全局变量
tom = Cat("tom")
print(tom.name)
# del可以删除一个对象
del tom
print("-"*50)