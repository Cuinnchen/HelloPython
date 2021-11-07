import socket
import multiprocessing
import re
import mini_frame

class WSGIServer(object):
    def __init__(self):
        # 1.创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)    $端口释放后会等待两分钟之后才能再被使用
        # 1.绑定
        self.tcp_server_socket.bind(('', 8888))
        self.tcp_server_socket.listen(128)

    def server_client(self,new_socket):
        """为这个客户端返回数据"""
        req = new_socket.recv(1024).decode('utf-8')
        print('>>>'*50)
        # print(req)
        req_lines = req.splitlines()
        print('>>'*20)
        print(req_lines)
        file_name = ''
        ret = re.match(r"[^/]+(/[^ ]*)", req_lines[0])
        print(ret)
        # ret = re.match(r"[^/]+(/[^ ]*)", [0],req_lines[0])
        if ret:
            file_name = ret.group(1)
            print("*"*50,file_name)
            if file_name == '/':
                file_name = "/index.html"

        # 2.返回http格式的数据，给浏览器
        # 准备发送给浏览器的数据  --header body
        # response = 'HTTP/1.1 200 OK\r\n'
        # response += '\r\n'
        # 如果请求的资源不是以.py结尾就认为是静态资源
        if not file_name.endswith('.py'):
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
            # new_socket.close()
        else:
            env = {}
            env['PATH_INFO'] = file_name
            body = mini_frame.application(env, self.set_response_header)  # 函数不带括号就是代表改方法本身不需要等方法执行
            header = 'HTTP/1.1 %s OK\r\n' % self.status
            for temp in self.headers:
                header += '%s:%s\r\n' % (temp[0],temp[1])

            header += '\r\n'
            response = header+body
            new_socket.send(response.encode('utf-8'))
        new_socket.close()

    def set_response_header(self,status, headers):
        self.status = status
        self.headers = [('Server','mini_server 1.0')]
        self.headers += headers


    def run_forever(self):

        while True:
            # 4.等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            p = multiprocessing.Process(target=self.server_client, args=(new_socket,))
            # 5.为这个客户端服务
            p.start()
            """
            多进程复制父进程资源,同时指向同一文件指示器，
            所以主进程需要关闭文件指示器
            而多线程共享全局变量，所以不需要在主线程中关闭
            """
            new_socket.close()

        self.tcp_server_socket.close()



def main():
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()

