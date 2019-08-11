# Web编程：CGI和WSGI 

## 相关模块

#### Web编程相关模块

模块/包|描述
------|----
Web应用程序|
cgi|从 CGI 获取数据
cgitb|处理 CGI 回溯消息
htmllib|用于解析简单 HTML 文件的老的 HTML 解析器;HTMLParser 类扩展自 sgmllib.SGMLParser 
HTMLParser|新的不基于 SGML 的 HTML、XHTML 解析器
htmlentitydefs|HTML 普通实体定义
Cookie|用于 HTTP 状态管理的服务器端 cookie
cookielib|HTTP 客户端的 cookie 处理类
webbrowser|控制器:向浏览器加载 Web 文档
sgmllib|解析简单的 SGML 文件
robotparser|解析 robots.txt 文件用于 URL 的“可获得性”分析
httplib|用来创建 HTTP 客户端
Web服务器|
BaseHttpServer|用来开发 Web 服务器的抽象类
SimpleHttpServer|处理最简单的 HTTP 请求(HEAD 和 GET)
CGIHTTPServer|既能像 SimpleHTTPServer 一样处理 Web 文件，又能处理 CGI(HTTP POST)请求
http.server|Python 3 中 BaseHTTPServer 、 SimpleHTTPServer 和 CGIHTTPServer 模块组合包的新名称 
wsgiref|WSGI 参考模块
第三方开发包（非标准库）|
BeautifulSoup|基于正则表达式的 HTML、XML 解析器，http://crummy.com/software/BeautifulSoup 
html5lib|HTML 5 解析器，http://code.google.com/p/html5lib
lxml|完整的 HTML 和 XML 解析器(支持以上两种解析器)http://lxml.de