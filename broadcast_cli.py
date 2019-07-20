# broadcast_cli.py
# 广播发送端
from socket import *
# 设置广播地址(通过ifconfig查看)
addr = ("172.40.91.255",9999)
# 创建UDP套接字      
s = socket(AF_INET, SOCK_DGRAM)
# 设置广播选项，允许进行广播通信
s.setsockopt(SOL_SOCKET, 
             SO_BROADCAST,1)
msg = "This is broadcast msg"
# 发送，目的地址为广播地址
s.sendto(msg.encode(), addr)
s.close()