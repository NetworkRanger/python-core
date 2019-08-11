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

## Web(HTTP)服务器

#### Web 服务器模块和类

模块|描述
----|---
BaseHTTPServer|提供基本的 Web 服务器和处理程序类，分别是 HTTPServer 和 BaseHTTPRequestHandler
SimpleHTTPServer|含有 SimpleHTTPRequestHandler 类，用于处理 GET 和 HEAD 请求
CGIHTTPSERVER|含有 CGIHTTPRequestHandler 类，用于处理 POST 请求并执行 CGI
http.server|前面的三个 Python 2 模块和类整合到一个 Python 3 包中

## 相关模块

#### Web 编程相关模块

模块/包|描述
------|-----
Web应用程序|
cgi|从标准网关接口(CGI)获取数据
cgitb|处理 CGI 返回数据
htmllib|老 HTML 解析器，用于解析简单的 HTML 文件;HTML-Parser 类扩展自 sgmllib.SGMLParser
HTMLparser|新的 HTML、XHTML 解析器，不基于 SGML
htmlentitydefs|一些 HTML 普通实体定义
Cookie|用于 HTTP 状态管理的服务器端 cookie
cookielib|HTTP 客户端的 cookie 处理类
webbrowser|控制器:向浏览器加载 Web 文档
sgmllib|解析简单的 SGML 文件
robotparser|解析 robots.txt 文件，对 URL 做“可获得性”分析
httplib|用来创建 HTTP 客户端
urllib|通过 URL 或相关工具访问服务器，在 Python 3 中，urllib.urlopen()被 urllib2.urlopen()替换，以 urllib.request.urlopen()的形式调用
urllib2；urllib.request、urllib.error|用于打开 URL 的类和函数，在 Python 3 中位于两个子包中 
urlparse、urlibparse|用于解析 URL 字符串的工具，在 Python 3 中重命名为 urllib.parse
XML处理|
xmllib|原来的简单 XML 解析器(已废弃) 
xml|包含许多不同解析器的 XML 包(见下文)
xml.sax|简单的 API，适用于兼容 SAX2 的 XML(SAX)解析器 
xml.dom|文档对象模型(DOM)XML 解析器
xml.etree|树形的 XML 解析器，基于 Element 灵活容器对象 
xml.parser.expat|非验证型 Expat XML 解析器的接口
xmlrpclib|通过 HTTP 提供 XML 远程过程调用(RPC)客户端
SimpleXMLRPCServer|Python XML-RPC 服务器的基本框架
DocXMLRPCServer|自描述 XML-RPC 服务器的框架
Web服务器|
BaseHTTPServer|用来开发 Web 服务器的抽象类
SimpleHTTPServer|处理最简单的 HTTP 请求(HEAD 和 GET)
CGIHTTPServer|不仅能像 SimpleHTTPServers 一样处理 Web 文件，还能处理 CGI(HTTP POST)请求
http.server|Python 3 中一个新的包名，合并了 Python 2 的 BaseHTTPServer、SimpleHTTPServer 和 CGIHTTPServer 模块
wsgiref|定义 Web 服务器和 Python Web 应用程序间标准接口的包
第三方开发包（非标准库）| 
HTMLgen|协助 CGI 把 Python 对象转换成可用的 HTML(http://starship.python.net/crew/friedrich/HTMLgen/ html/main.html)
BeautifulSoup|HTML、XML 解析器及转换器 (http://crummy.com/software/BeautifulSoup)
Mechanize|基于万维网的 Web 浏览包 (http://wwwsearch.sourceforge.net/mechanize/)                                                                                                                        