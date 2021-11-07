import socket
import time

tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server_socket.bind(('',1234))
tcp_server_socket.listen(128)
# 设置套接字为非堵塞
tcp_server_socket.setblocking(False)

client_socket_list = list()

while True:
    time.sleep(0.5)
    try:
        new_socket, new_addr = tcp_server_socket.accept()
    except Exception as ret:
        print('------没有新的客户端到来------')
    else:
        print('只要没有产生异常，意味着来了一个新的客户端')
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)

    for client in client_socket_list:
        try:
            recv_data = client.recv(1024)
        except Exception as ret:
            print('----这个客户端没有发送过来数据')
        else:
            print('----没有异常----')
            print(recv_data)
            if recv_data:
                print('-----客户端发来了数据-----')
            else:
                client.close()
                client_socket_list.remove(client)