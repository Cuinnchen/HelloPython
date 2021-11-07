import time
import re

URL_FUNC_DICT = dict()
func_list = list()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT['index.py] = index
        URL_FUNC_DICT[url]= func
        def call_func(*args,**kwargs):
            return func(*args,**kwargs)
        return call_func
    return set_func

@route('/index.html')
# @route('/index.py')
def login():
    return "welcome to our website.... time: %s" % time.ctime()

def register():
    return "welcome to our register.... time: %s" % time.ctime()

def profile():
    return "welcome to our profile.... time: %s" % time.ctime()

# URL_FUNC_DICT ={
#     "/index.py": login,
#     "/register.py": register
# }

# 装饰器实现↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑


def application(env, start_response):
    """WSGI协议"""
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    # if env['PATH_INFO'] == '/login.py':
    #     return login()
    # elif env['PATH_INFO'] == '/register.py':
    #     return register()
    # else:
    #     return 'Hello World! 我爱你中国'
    try:
        # func =URL_FUNC_DICT[file_name]
        # return func()
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常 %s" % str(ret)


