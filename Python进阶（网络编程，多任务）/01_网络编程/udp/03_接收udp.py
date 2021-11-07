from socket import *

def main():
    # 创建UDP套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    # 绑定本地的相关信息，如果一个网络程序不绑定
    localaddr = ('',7788)
    udp_socket.bind(localaddr)
    # 接收数据
    recv_data = udp_socket.recvfrom(1024)
    recv_msg = recv_data[0]   # 数据
    send_addr = recv_data[1]  #发送方的地址
    # 打印接收到的数据
    print('%s:%s' % (str(send_addr),recv_msg.decode('gbk')))
    print(recv_data)
    # 关闭套接字
    udp_socket.close()

