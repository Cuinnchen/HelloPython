def set_xx(func):
    print('开始进行装饰1')
    def call_func(*args,**kwargs):
        print('--这是装饰1--')
        return func(*args,**kwargs)
    return call_func


def set_qx(func):
    print('开始进行装饰2')
    def call_func(*args,**kwargs):
        print('--这是装饰2--')
        return func(*args,**kwargs)
    return call_func

@set_xx
@set_qx # 先运行下面的装饰器，装饰器先运作靠近函数的装饰器  test = set_qx(test)
def test(num,*args,**kwargs):
    print('-----1-----%d' % num)
    return 'ok' ,'200'

# @set_func
# def test1():
#     pass

ret = test(100)

# ret = test()
print(ret)



