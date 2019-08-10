# 网络编程

## Python中的网络编程

### 套接字对象(内置)方法

#### 常见的套接字对象方法和属性

名称|描述
---|----
服务器套接字方法|
s.bind()|将地址(主机名、端口号对)绑定到套接字上
s.listen()|设置并启动 TCP 监听器
s.accept()|被动接受 TCP 客户端连接，一直等待直到连接到达(阻塞)
客户端套接字方法|
s.connect()|主动发起 TCP 服务器连接 
s.connect_ex()|connect()的扩展版本，此时会以错误码的形式返回问题，而不是抛出一个异常
普通的套接字方法|
s.recv()|接收 TCP 消息
s.recv_into()|接收 TCP 消息到指定的缓冲区
s.send()|发送 TCP 消息
s.sendall()|完整地发送 TCP 消息
s.recvfrom()|接收 UDP 消息
s.recvfrom_into()|接收 UDP 消息到指定的缓冲区
s.sendto()|发送 UDP 消息
s.getpeername()|连接到套接字(TCP)的远程地址
s.getsockname()|当前套接字的地址
s.getsockopt()|返回给定套接字选项的值
s.setsockopt()|设置给定套接字选项的值
s.shutdown()|关闭连接
s.close()|关闭套接字
s.detach()| 在未关闭文件描述符的情况下关闭套接字，返回文件描述符 
s.ioctl()|控制套接字的模式(仅支持 Windows)
面向阻塞的套接字方法|
s.setblocking()|设置套接字的阻塞或非阻塞模式
s.settimeout()|设置阻塞套接字操作的超时时间
s.gettimeout()|获取阻塞套接字操作的超时时间
面向文件的套接字方法|
s.fileno()|套接字的文件描述符
s.makefile()|创建与套接字关联的文件对象
数据属性|
s.family|套接字家族
s.type|套接字类型
s.proto|套接字协议

### socket模块属性

#### socket 模块属性

属性名称|描述
-------|---
数据属性|
AF_UNIX、AF_INET、AF_INET6、AF_NETLINK、AF_TIPC|Python中支持的套接字地址家族 
SO_STREAM、SO_DGRAM|套接字类型(TCP=流，UDP=数据报)
has_ipv64|指示是否支持 IPv6 的布尔标记
异常|
error|套接字相关错误
herror|主机和地址相关错误
gaierror|地址相关错误
timeout|超时时间
函数|
socket()|以给定的地址家族、套接字类型和协议类型(可选)创建一个套接字对象
socketpair()|以给定的地址家族、套接字类型和协议类型(可选)创建一对套接字对象
create_connection()|常规函数，它接收一个地址(主机名，端口号)对，返回套接字对象
fromfd()|以一个打开的文件描述符创建一个套接字对象
ssl()|通过套接字启动一个安全套接字层连接;不执行证书验证
getaddrinfo()|获取一个五元组序列形式的地址信息
getnameinfo()|给定一个套接字地址，返回(主机名，端口号)二元组
getfqdn()|返回完整的域名
gethostname()|返回当前主机名
gethostbyname()|将一个主机名映射到它的 IP 地址               
gethostbyname_ex()|gethostbyname()的扩展版本，它返回主机名、别名主机集合和 IP 地址列表
gethostbyaddr()|将一个 IP 地址映射到 DNS 信息;返回与 gethostbyname_ex()相同的 3 元组
getprotobyname()|将一个协议名(如‘tcp’)映射到一个数字
getservbyname()/getservbyport()|将一个服务名映射到一个端口号，或者反过来;对于任何一个函数来说，协议名都是可 选的
ntohl()/ntohs()|将来自网络的整数转换为主机字节顺序
htonl()/htons()|将来自主机的整数转换为网络字节顺序
inet_aton()/inet_ntoa()|将 IP 地址八进制字符串转换成 32 位的包格式，或者反过来(仅用于 IPv4 地址)
inet_pton()/inet_ntop()|将 IP 地址字符串转换成打包的二进制格式，或者反过来(同时适用于 IPv4 和 IPv6 地址)
getdefaulttimeout()/setdefaulttimeout()|以秒(浮点数)为单位返回默认套接字超时时间;以秒(浮点数)为单位设置默认套接 字超时时间


## SocketServer模块

#### SocketServer 模块类
             
类|描述 
---|---              
BaseServer|包含核心服务器功能和 mix-in 类的钩子;仅用于推导，这样不会创建这个类的实例;可以用 TCPServer 或 UDPServer 创建类的实例
TCPServer/UDPServer|基础的网络同步 TCP/UDP 服务器
UnixStreamServer/UnixDatagramServer|基于文件的基础同步 TCP/UDP 服务器核心派出或线程功能;只用作 mix-in 类与一个服务器类配合实现一些异步性;不能直接实例化这个类
ForkingMixIn/THreadingMixIn|ForkingMixIn 和 TCPServer/UDPServer 的组合 
ThreadingTCPServer/ThreadingUDPServer|ThreadingMixIn 和 TCPServer/UDPServer 的组合
BaseRequestHandler|包含处理服务请求的核心功能;仅仅用于推导，这样无法创建这个类的实例; 可以使用 StreamRequestHandler 或 DatagramRequestHandler 创建类的实例
StreamRequestHandler/DatagramRequestHandler|实现 TCP/UDP 服务器的服务处理器

## 相关模块

#### 网络/套接字编程相关模块

模块|描述
----|---
socket|它是低级网络编程接口
asyncore/asynchat|提供创建网络应用程序的基础设施，并异步地处理客户端 
select|在一个单线程的网络服务器应用中管理多个套接字连接
SocketServer|高级模块，提供网络应用程序的服务器类，包括 forking 或 threading 簇
