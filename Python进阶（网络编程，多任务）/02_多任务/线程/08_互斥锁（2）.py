import threading
import time

# 定义一个全局变量
g_num = 0

def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print('------in test1 g_num=%s---' % str(num))


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire() # 加锁
        g_num += 1
        mutex.release() # 解锁
    print('-----in test2 g_num=%s----' % str(num))

# 创建一个互斥锁，默认没有锁定
mutex = threading.Lock()


def main():
    # target指定将来 这个线程去哪个函数执行代码
    # args指定将来调用函数的时候 传递什么数据过去
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()
    # 等待上面的2个线程执行完毕
    time.sleep(2)
    print(' in main Thread g_num = %d' % g_num)
if __name__ == '__main__':
    main()
    # a = (g_num,)
    # print(a)