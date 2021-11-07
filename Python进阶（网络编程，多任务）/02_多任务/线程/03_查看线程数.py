import threading
import time


def test1():
    for i in range(5):
        print('----test1---%d---' % i)
        time.sleep(1)
    # 如果创建Thread时执行的函数，运行结束那么意味着 这个子线程结束了。。

# def test2():
#     for i in range(10):
#         print('----test2---%d---' % i)
#         time.sleep(1)

def main():
    # 在调用Thread之前先打印线程信息
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)
    # t2 = threading.Thread(target=test2)

    # 在调用Thread之后先打印线程信息
    print(threading.enumerate())
    t1.start()
    # 在调用start之后先打印线程信息
    print(threading.enumerate())
    # time.sleep(1)
    # print("----1----")
    # t2.start()

    # time.sleep(1)
    # print("----2----")

    # while True:
    #     print(threading.enumerate())
    #     if len(threading.enumerate()) <= 1:
    #         break
    #     time.sleep(1)
if __name__ == '__main__':
    main()

    """
    当调用Thread不会创建线程
    当调用Thread创建出来的实例对象的start方法的时候，才会创建线程已经
    让这个线程开始运行
    """