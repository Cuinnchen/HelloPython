class Cat(object):

    def eat(self):
        print("%s 爱吃鱼"% self.name)

    def drink(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("小猫爱喝水")


tom = Cat()

# 可以使用 .属性名 利用赋值语句就可以
tom.name = "Tom"
tom.drink()
tom.eat()

print(tom)

# 在创建一个猫对象

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.drink()
lazy_cat.eat()
print(lazy_cat)
