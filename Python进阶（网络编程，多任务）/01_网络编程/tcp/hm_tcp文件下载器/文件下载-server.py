import socket

def send_file_2_client(new_client_socket,client_addr):
    # 接收客户端发送过来的 要下载的文件名
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客户端（%s）需要下载的文件是：%s' % (str(client_addr), file_name))
    # 发送文件的数据给客户端
    # 打开文件，读取数据
    file_content = None
    try:
        f = open(file_name,'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('没有要下载的文件（%s）' % ret)

    if file_content:
        new_client_socket.send(file_content)

def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定本地信息
    tcp_server_socket.bind(('192.168.0.105',7890))
    # 3.让默认套接字由主动变为被动 listen
    tcp_server_socket.listen(128)
    while True:
        # 返回一个元组
        # 4.等待客户端连接
        new_client_socket,client_addr = tcp_server_socket.accept()
        # 5.调用发送文件函数
        send_file_2_client(new_client_socket,client_addr)
    tcp_server_socket.close()



if __name__ == '__main__':
    main()
