from hm_模块和包 import hm_01_测试模块1 as DogModule
from hm_模块和包 import hm_02_测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog
print(dog)

cat = CatModule.Cat()
print(cat)