def set_func(func):
    def call_func():
        print('--权限验证--')
        print('--权限验证--')
        func()
    return call_func


@set_func
def test():
    print('-----1-----')

test()