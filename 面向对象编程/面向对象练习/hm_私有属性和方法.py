class Women:

    def __init__(self,name):

        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name,self.__age))

xiaofang =Women("小芳")

# 私有属性在外界不能够被直接访问
# print(xiaofang.__age)

# 私有方法，同样不允许在外界直接访问
xiaofang.__secret()