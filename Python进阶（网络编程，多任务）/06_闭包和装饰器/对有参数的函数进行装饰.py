def set_func(func):
    def call_func(*args,**kwargs):
        print('--权限验证--')
        print('--权限验证--')
        func(*args,**kwargs)
    return call_func


@set_func
def test(num,*args,**kwargs):
    print('-----1-----%d' % num)
    print('-----1-----' ,args)
    print('-----1-----' , kwargs)

ret = test(100)

print(ret)

