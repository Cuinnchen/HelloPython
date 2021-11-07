def set_fun_1(fun):
    def call_fun():
        return  '<h1>' + fun() + "</h1>"
    return call_fun

class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('这里是装饰器添加的功能。。')
        return self.func()
@Test
def get_str():
    return 'haha'


print(get_str())