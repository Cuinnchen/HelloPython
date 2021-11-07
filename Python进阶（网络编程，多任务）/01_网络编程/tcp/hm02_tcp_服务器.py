import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(('192.168.0.106',7890))
    tcp_server_socket.listen(128)
    # 返回一个元组
    new_client_socket,client_addr = tcp_server_socket.accept()
    print(client_addr)

    # 接收客户端发送过来的请求
    recv_data = new_client_socket.recv(1024)

    print(recv_data)

    new_client_socket.send('1111'.encode('utf-8'))

    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()

