import socket

def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(('',9090))
    while True:
    # 从键盘获取数据
        send_data = input("请输入要发送的数据： ")
        if send_data == 'exit':
            break
        # 可以使用套接字收发数据
        udp_socket.sendto(send_data.encode("utf-8"),('192.168.0.105',7788))
        # 关闭套接字
    udp_socket.close()
    print("-------run--------")
if __name__ == '__main__':
    main()