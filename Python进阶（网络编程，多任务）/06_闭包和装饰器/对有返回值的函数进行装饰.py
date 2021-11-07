def set_func(func):
    def call_func(*args,**kwargs):
        print('--权限验证--')
        print('--权限验证--')
        return func(*args,**kwargs)
    return call_func
# 通用装饰器

# @set_func
def test(num,*args,**kwargs):
    print('-----1-----%d' % num)
    print('-----1-----' ,args)
    print('-----1-----' , kwargs)
    return 'ok' ,'200'

# @set_func
# def test1():
#     pass

ret = test(100)

# ret = test()
print(ret)


