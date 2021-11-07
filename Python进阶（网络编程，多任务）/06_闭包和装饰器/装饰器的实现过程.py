import time

# def set_func(func):
#     def call_func():
#         print('--权限验证--')
#         print('--权限验证--')
#         func()
#     return call_func



def test():
    print('-----1-----')

# test1 = set_func(test)
# test()
# test()
 #  统计函数运行时间

def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        end_time = time.time()
        print('all tine %f' % (end_time-start_time))
    return call_func
@set_func  # 等价于 test =set_func(test)
def test():
    print('-----1-----')

test()