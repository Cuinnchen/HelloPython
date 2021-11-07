import socket

def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 获取对方的ip/port
    dest_ip = input('请输入ip')
    try:
        dest_port = int(input('请输入对方port'))
    except ValueError:
        dest_port = int(input('请输入对方port(数字)'))
    send_data = input("请输入要发送的数据")
    # 可以使用套接字收发数据
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))
    # 接收返回过来的数据
    udp_data = udp_socket.recvfrom(1024)
    # 套接字可以同时收发数据
    print(udp_data)
    # 关闭套接字
    udp_socket.close()
    print("-------run--------")
if __name__ == '__main__':
    main()