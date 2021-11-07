import socket
import threading


def recv_msg(udp_socket):
    while True:
        reve_data = udp_socket.recvfrom(1024)
        print(reve_data)

def send_msg(udp_socket,dest_ip,dest_port):
    while True:
        send_data = input('输入要发送的数据：')
        udp_socket.sendto(send_data.encode('utf-8'),(dest_ip, dest_port))

def main():
    """完成udp聊天器的整体控制"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(('',9870))

    # 获取对方ip
    dest_ip = input('ip:')
    dest_port = int(input('port:'))

    # 创建线程
    t1 = threading.Thread(target=recv_msg, args=(udp_socket,))
    t2 = threading.Thread(target=send_msg, args=(udp_socket,dest_ip,dest_port))

    t1.start()
    t2.start()
if __name__ == '__main__':
    main()