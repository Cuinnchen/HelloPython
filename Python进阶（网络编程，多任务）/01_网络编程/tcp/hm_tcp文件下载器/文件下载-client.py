import  socket

def main():

    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.获取服务器的ip port
    dest_ip = input('请输入下载服务器的IP:')
    dest_port = input('请输入下载服务器的端口：')
    # 3.链接服务器
    tcp_socket.connect((dest_ip,int(dest_port)))
    # 4.获取下载的文件名字
    download_file_name = input('请输入要下载的文件名字：')

    # 5.将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode('utf-8'))

    # 6.接收文件中的数据
    recv_data = tcp_socket.recv(1024)

    # 7.保存接收到的数据到一个文件中
    if recv_data:
        with open('[下载]' + download_file_name,'wb') as f:
            f.write(recv_data)
    # 8.关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()