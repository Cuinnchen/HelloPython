class Cat(object):
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


tom = Cat()
tom.drink()
tom.eat()

print(tom)

# 在创建一个猫对象

lazy_cat =Cat()

lazy_cat.drink()
lazy_cat.eat()
print(lazy_cat)

