import socket
# import threading
# import time

def main():
    # 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 链接服务器
    tcp_socket.connect(('192.168.0.106', 1234))
    # 发送/接收数据
    send_data = input('你要发送的数据')
    tcp_socket.send(send_data.encode('utf-8'))
    sever_data = tcp_socket.recv(1024)
    print(sever_data)
    # 关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    # for i in range(10):
    #     time.sleep(1)
    #     t = threading.Thread(target=main)
    #     t.start()
    main()
