import socket

def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 可以使用套接字收发数据
    udp_socket.sendto(b"TT",('192.168.0.103',8080))
    # 关闭套接字
    udp_socket.close()
    print("-------run--------")
if __name__ == '__main__':
    main()