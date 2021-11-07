def line(k, b):
    def create_y(x):
        print(k*x+b)
    return create_y


l = line(1,2)
l(0)
# 在函数内部再定义一个函数，
# 并且这个函数用到了外边函数的变量，
# 那么将这个函数以及用到的一些变量称之为闭包