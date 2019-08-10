# 因特网客户端编程

## 文件传输

### ftplib.FTP类的方法

#### FTP对象的方法

方法|描述
---|---
login(user='anonymous', passwd='', acct='')|登录 FTP 服务器，所有参数都是可选的
pwd()|获得当前工作目录
cwd(path)|把当前工作目录设置为 path 所示的路径
dir ([path[,...[,cb]])|显示 path 目录里的内容，可选的参数 cb 是一个回调函数，会传递给 retrlines()方法
nlst ([path[,...])|与 dir()类似，但返回一个文件名列表，而不是显示这些文件名
retrlines(cmd [, cb])|给定 FTP 命令(如“RETR filename”)，用于下载文本文件。可选的回调函数 cb 用于处理文件的每一行
retrbinary(cmd, cb[,bs=8192[, ra]])|与 retrlines()类似，只是这个指令处理二进制文件。回调函数 cb 用于处理每一块(块大小默认为 8KB) 下载的数据
storlines(cmd, f)|给定 FTP 命令(如“STOR filename”)，用来上传文本文件。要给定一个文件对象 f
storbinary(cmd, f [,bs=8192])|与 storlines()类似，只是这个指令处理二进制文件。要给定一个文件对象 f，上传块大小 bs 默认为 8KB
rename(old, new)|把远程文件old重命名为new
delete(path)|删除位于path的远程文件
mkd(directory)|创建远程目录 
rmd(directory)|删除远程目录
quit()|关闭连接并退出

## 网络新闻

### nntplib.NNTP类的方法

#### NNTP 对象的方法
 
方法|描述
----|---
 group(name)|选择一个组的名字，返回一个元组(rsp,ct,fst,lst,group)，分别表示服务器响应信息、文章数量、第一个和最后一个文章的编号、组名，所有数据都是字符串。(返回的 group 与传进去的 name 应该是相同的)
xhdr(hdr, artrg[, ofile])|返回文章范围 artrg(“头 -尾”的格式)内文章 hdr 头的列表，或把数据输出到文件 ofile 中
body(id[, ofile])|根据 id 获取文章正文，id 可以是消息的 ID(放在尖括号里)，也可以是文章编号(以字符串形式表 示)，返回一个元组(rsp, anum, mid, data)，分别表示服务器响应信息、文章编号(以字符串形式表示)、 消息 ID(放在尖括号里)、文章所有行的列表，或把数据输出到文件 ofile 中
head(id)|与 body()类似，返回相同的元组，只是返回的行列表中只包括文章标题
article(id)|同样与 body()类似，返回相同的元组，只是返回的行列表中同时包括文章标题和正文
stat(id)|让文章的“指针”指向 id(即前面的消息 ID 或文章编号)。返回一个与 body()相同的元组(rsp, anum, mid)，但不包含文章的数据
next()|用法和 stat()类似，把文章指针移到下一篇文章，返回与 stat()相似的元组
last()|用法和 stat()类似，把文章指针移到最后一篇文章，返回与 stat()相似的元组
post(ufile)| 上传 ufile 文件对象里的内容(使用 ufile.readline())，并发布到当前新闻组中
quit()|关闭连接并退出
 
## 电子邮件

### smtplib.SMTP类方法

#### SMTP 对象常见的方法

方法|描述
----|----
sendmail(from ,to, msg[, mopts, ropts])|将 msg 从 from 发送至 to(以列表或元组表示)，还可以选择性地设置 ESMTP 邮件(mopts)和收件人(ropts)选项
ehlo()或helo()|使用 EHLO 或 HELO 初始化 SMTP 或 ESMTP 服务器的会话。这是可选的，因为sendmail()会在需要时自动调用相关内容
starttls(keyfile=None, certfile=None)|让服务器启用 TLS 模式。如果给定了 keyfile 或 certfile，则它们用来创建安全套接字
set_debuglevel(level)|为服务器通信设置调试级别
quit()|关闭连接并退出
login(user, passwd)|使用用户名和密码登录 SMTP 服务器

### poplib.POP3 类方法


#### POP3 对象的常用方法
方法|描述
----|----
user(login)|向服务器发送登录名，并显示服务器的响应，表示服务器正在等待输入该用户的密码 
pass_(passwd)|在用户使用 user()登录后，发送 passwd。如果登录失败，则抛出异常
stat()|返回邮件的状态，即一个长度为2的元组(msg_ct, mbox_siz)，分别表示消息的数量和消息的总大小(即 字节数)
list([msgnum])|stat()的扩展，从服务器返回以三元组表示的整个消息列表(rsp, msg_list, rsp_siz)，分别为服务器的响应、 消息列表、返回消息的大小。如果给定了 msgnum，则只返回指定消息的数据
retr(msgnum)|从服务器中得到消息的 msgnum，并设置其“已读”标志。返回一个长度为 3 的元组(rsp, msglines, msgsiz)， 分别为服务器的响应、消息的 msgnum 的所有行、消息的字节数
dele(msgnum)|把消息 msgnum 标记为删除，大多数服务器在调用 quit()后执行删除操作 
quit()|注销、提交修改(如处理“已读”和“删除”标记等)、解锁邮箱、终止连接，然后退出


### imaplib.IMAP4 类中的常用方法

#### IMAP4 对象的常见方法
close()|关闭当前邮箱。如果访问权限不是只读，则本地删除的邮件在服务器端也会被丢弃
fetch(message_set, message_parts)|获取之前由 message_set 设置的电子邮件消息状态(或使用 message_parts 获取部分状态信息)
login(user, password)|使用指定的用户名和密码登录
logout()|从服务器注销
noop()|ping 服务器，但不产生任何行为
search(charset, *criteria)|查询邮箱中至少匹配一块 criteria 的消息。如果 charset 为 False，则默认使用 US-ASCII
select(mailbox= 'INBOX ', read-only=False)|选择一个文件夹(默认是 INBOX)，如果是只读，则不允许用户修改其中的内容


## 相关模块

### 电子邮件

#### 电子邮件相关模块

模块包|描述
-----|---
email|用于处理电子邮件的包(也支持 MIME)
smtpd|SMTP 服务器
base64|Base-16、32、64 数据编码(RFC 3548) 
mhlib|处理 MH 文件夹和消息的类
mailbox|支持 mailbox 文件格式解析的类 
mailcap|“mailcap”文件的处理模块
mimetools|(废弃)MIME 消息解析工具(使用上面的 email 模块)
mimetypes|在文件名/URL 和相关的 MIME 类型之间转换的模块
MimeWriter|(废弃)MIME 消息处理模块(使用上面的 email 模块)
mimify|(废弃)MIME 消息处理工具(使用上面的 email 模块)
quopri|对 MIME 中引号括起来的可打印数据进行编码或解码
binascii|二进制和 ASCII 转换
binhex|Binhex4 编码和解码支持

### 其他因特网客户端协议

#### 因特网客户端协议相关模块

模块|描述
----|----
ftplib|FTP 协议客户端
xmlrpclib|XML-RPC 协议客户端
httplib|HTTP 和 HTTPS 协议客户端
imaplib|IMAP4 协议客户端
nntplib|NNTP 协议客户端
poplib|POP3 协议客户端
smtplib|SMTP 协议客户端
  
  
  
  
   