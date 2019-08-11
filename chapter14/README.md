# 文本处理

## JSON

#### JSON和Python类型之间的区别

JSON|Python 2|Python 3
----|--------|--------
object|dict|dict
array|list tuple|list tuple
string|unciode|str
number(int)|int,long|int
number(real)|float|float
true|True|True
false|False|False
null|None|None

## 相关模块

#### 与文本处理相关的模块

模块|包
----|---
csv|逗号分割值的处理
SimpleXMLRPCServer|XML-RPC 服务器(在 Python 3 中合并进 xmlrpc.server 中) 
DocXMLRPCServer|自归档的 XML-RPC 服务器(在 Python 3 中合并进 xmlrpc.server 中) 
xmlrpclib|XML-RPC 客户端(在 Python 3 中重命名为 xmlrpc.client)
json|JSON 编码和加码工具(在 Python 2.6 之前是外部包 simplejson) 
xml.parsers.expat|快速无验证的 XML 解析器
xml.dom|基于树/DOM 的 XML 解析
xml.sax|基于事件/流的 XML 解析
xml.etree.ElementTree|ElementTree XML 解析器和树构建器