import socket


def server_client(new_socket):
    """为这个客户端返回数据"""
    request = new_socket.recv(1024)
    print(request)

    # 2.返回http格式的数据，给浏览器
    # 准备发送给浏览器的数据  --header body
    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'
    response += '<h1>haha</1>'
    new_socket.send(response.encode('utf-8'))

    # 关闭套接字
    new_socket.close()

def main():
    # 1.创建套接字
    tcp_server_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 1.绑定
    tcp_server_socket.bind(('', 8888))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    while True:
    # 4.等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5.为这个客户端服务
        server_client(new_socket)

    tcp_server_socket.close()



if __name__ == '__main__':
    main()