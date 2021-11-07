import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(('192.168.0.103',7890))
    tcp_server_socket.listen(128)

    # 返回一个元组
    while True: # 为多个客户端服务
        print("等待新的客户端到来")
        new_client_socket,client_addr = tcp_server_socket.accept()
        print("一个客户端已经到来%s" % str(client_addr))
        while True: # 循环多次为同一个客户端服务
        # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端发送的请求%s" % recv_data.decode('utf-8'))
            # 如果reve解堵塞：
            # 1.客户端发送过来数据
            # 2.客户端调用close导致 这个recv解堵塞
            if recv_data:
                new_client_socket.send('1111'.encode('utf-8'))
            else:
                break
            new_client_socket.close()
            print('已经服务完毕')
    tcp_server_socket.close()
    print(11111)


if __name__ == '__main__':
    main()

