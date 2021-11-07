import threading
import time

# 定义一个全局变量
# g_num = 100

def test1(num):
    num.append(33)
    print('------in test1 g_num=%s---' % str(num))


def test2(num):
    print('-----in test2 g_num=%s----' % str(num))


g_num = [11,22]

def main():
    # target指定将来 这个线程去哪个函数执行代码
    # args指定将来调用函数的时候 传递什么数据过去
    t1 = threading.Thread(target=test1, args=(g_num,))
    t2 = threading.Thread(target=test2, args=(g_num,))
    t1.start()
    time.sleep(1)

    t2.start()
    # print(' in main Thread g_num = %d' % g_num)
if __name__ == '__main__':
    main()
    # a = (g_num,)
    # print(a)