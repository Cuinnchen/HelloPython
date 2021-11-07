import socket
import re

def server_client(new_socket,req):
    """为这个客户端返回数据"""
    # req = new_socket.recv(1024).decode('utf-8')
    # print('>>>'*50)
    # # print(req)
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
        # print(html_content)
        f.close()
        print('1111111111')
        # 2.1 准备发送给浏览器的数据---header
        response_body = html_content
        print('222222222222')
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        print('3333333333333')
        response_header += '\r\n'
        # s = response_header.encode('utf-8')
        # print(type(s))
        print(type(response_body))
        print(type(response_header))
        response = response_header.encode('utf-8') + response_body
        print('444444444444444')

        # 将response header发送给浏览器
        new_socket.send(response)
        print('55555555555555')
        # 将response body发送给浏览器

    # new_socket.close()

def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 1.绑定
    tcp_server_socket.bind(('', 8889))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞
    client_socket_list = list()
    while True:
    # 4.等待新客户端的链接
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode('utf-8')
            except Exception as ret:
                pass
            else:
                if recv_data:
                    server_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    tcp_server_socket.close()



if __name__ == '__main__':
    main()