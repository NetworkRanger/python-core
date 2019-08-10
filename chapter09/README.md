# Web客户端和服务器

## Python Web客户端工具

### 统一资源定位符

#### Web 地址的各个组件

URL组件|描述
-------|---
prot_sch|网络协议或下载方案
net_loc|服务器所在地(也许含有用户信息)
path|使用斜杠(/)分割的文件或CGI 应用的路径
params|可选参数 
query|连接符(&)分割的一系列键值对
frag|指定文档内特定锚的部分

#### 网络地址的各个组件

组件|描述
----|---
user|用户名或登录
passwd|用户密码
host|运行 Web 服务器的计算机名称或地址(必需的)
port|端口号(如果不是默认的 80)

### urlparse模块

#### urlparse 模块中的核心函数
urlparse函数|描述
------------|---
urlparse(urlstr defProtSch=None, allowFrg=None)|将 urlstr 解析成各个组件，如果在 urlstr 中没有给定协议或者方案，则使用 defProtSch;allowFrag 决定是否允许有 URL 片段
urlunparse(urltup)|将 URL 数据(urltup)的一个元组拼成一个 URL 字符串
urljoin(baseurl, newurl, allowFrag=None)|将 URL 的根域名和 newurl 拼合成一个完整的 URL;allowFrag 的作用和 urlpase()相同

### urllib模块

#### urllib.urlopen()文件类型对象的方法

urlopen()对象方法|描述
----------------|---
f.read([bytes])|从 f 中读出所有或 bytes 个字节
f.readline()|从 f 中读取一行
f.readlines()|从 f 中读出所有行，作为列表返回
f.close()|关闭f的URL连接
f.fileno()|返回 f 的文件句柄
f.info()|获得f的MIME头文件
f.geturl()|返回f的真正URL

#### urllib 模块中的核心函数

urllib 函数|描述
-----------|----
urlopen(urlstr, postQueryData=None)|打开 URL urlstr，如果是 POST 请求，则通过 postQueryData 发送请求的数据
urlretrieve(urlstr, localfile=None,downloadStatusHook=None)| 将URL urlstr中的文件下载到localfile或临时文件中(如果没有指定localfile);如果函数正在执行，downloadStatusHook 将会获得下载的统计信息
quote(urldata, safe='/')|对 urldata 在 URL 里无法使用的字符进行编码，safe 中的字符无须编码
quote_plus(urldata, safe='/')|除了将空格编译成加(+)号(而非%20)之外，其他功能与 quote()相似
unquote(urldata)|将 urldata 中编码过的字符解码
unquote_plus(urldata)|除了将加号转换成空格，其他功能与 unquote()相同
urlencode(dict)|将 dict 的键值对通过 quote_plus()编译成有效的 CGI 查询字符串，用 quote_plus()对 这个字符串进行编码