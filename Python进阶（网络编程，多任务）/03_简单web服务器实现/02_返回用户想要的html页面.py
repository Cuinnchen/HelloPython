import socket
import re

def server_client(new_socket):
    """为这个客户端返回数据"""
    req = new_socket.recv(1024).decode('utf-8')  # 接受客户端返回数据
    print('>>>'*50)
    print('req----------',req)
    req_lines = req.splitlines()
    print('>>'*20)
    print(req_lines)
    file_name = ''
    ret = re.match(r"[^/]+(/[^ ]*)",req_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*"*50,file_name)
        if file_name == '/':
            file_name = "/index.html"

    # 2.返回http格式的数据，给浏览器
    # 准备发送给浏览器的数据  --header body
    # response = 'HTTP/1.1 200 OK\r\n'
    # response += '\r\n'
    try:
        f = open("../html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据---header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # 2.2 准备发送给浏览器的数据---boy
        # response += "hahahhah"

        # 将response header发送给浏览器
        new_socket.send(response.encode("utf-8"))
        # 将response body发送给浏览器
        new_socket.send(html_content)
    new_socket.close()

def main():
    # 1.创建套接字
    tcp_server_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    # 1.绑定
    tcp_server_socket.bind(('', 8888))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    while True:
    # 4.等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5.为这个客户端服务
        server_client(new_socket)

    tcp_server_socket.close()



if __name__ == '__main__':
    main()