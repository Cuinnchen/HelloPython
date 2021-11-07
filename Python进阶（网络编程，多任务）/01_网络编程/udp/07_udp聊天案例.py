import socket


def send_msg(udp_socket):
        dest_ip = input('请输入对方的ip：')
        dest_port = int(input('请输入对方的端口：'))
        send_data = input('请输入要发送的信息：')
        udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))

def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode('utf-8')))

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(('', 7788))
    # 循环来进行处理事情
    while True:
        print("------chat-----")
        print('1发送消息')
        print('2接收消息')
        print('0退出')
        op = input("请输入功能：")
        if op =='1':
            send_msg(udp_socket)
        elif op =='2':
            recv_msg(udp_socket)
        elif op == '0':
            break
        #
        # send_msg(udp_socket)
        #
        # recv_msg(udp_socket)


if __name__ == '__main__':
    main()