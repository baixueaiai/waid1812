# broadcast_svr.py
# 广播接收端
from socket import *
# 创建一个UDP套接字
s = socket(AF_INET, SOCK_DGRAM)
# 设置端口复用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",9999))
print("接受端已启动")
while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("收到消息:", msg.decode())
    except:
        print("接收出错")
        break
s.close()  #关闭socket