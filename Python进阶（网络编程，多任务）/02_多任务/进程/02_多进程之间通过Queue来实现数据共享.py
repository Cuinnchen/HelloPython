import multiprocessing
import time
import os


def download(q):
    data = [11,22,33,44]
    # print('Process to write: %s' % os.getpid())
    for temp in data:
        # print('Put %s from queue.' % temp)
        q.put(temp)
    # time.sleep(0.1)
    # print('11111',q.qsize())
    print('下载器已经下载完了并且保存在队列中')



def analysit_data(q):
    # print('Process to read: %s' % os.getpid())
    # 从队列中获取数据
    waiting_analysis_data = []
    # print(f"还未下载{waiting_analysis_data}")
    # print('22222',q.qsize())
    while True:
        data = q.get()
        # print('22223', q.qsize())
        # print('Get %s from queue.' % data)
        waiting_analysis_data.append(data)
        if q.empty():
            # print(q.qsize())
            print(q.empty())
            break

    print(waiting_analysis_data)

def main():
    # 1.创建一个队列
    q = multiprocessing.Queue()
    # 2.创建多个进程，将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download, args=(q,))
    p2 = multiprocessing.Process(target=analysit_data, args=(q,))

    p1.start()
    p2.start()
    p2.join()    # p2.terminate()

if __name__ == '__main__':
    main()