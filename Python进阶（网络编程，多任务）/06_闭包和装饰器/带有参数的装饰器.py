def set_level(level_num):
    def set_func(func):
        def call_func(*args,**kwargs):
             if level_num == 1:
                 print('--权限验证1，验证--')
             elif level_num ==2:
                 print('--权限验证2--')
             return func(*args, **kwargs)
        return call_func
    return set_func


@set_level(2)
def test():
    print('---test---')
    return 'ok'



test()