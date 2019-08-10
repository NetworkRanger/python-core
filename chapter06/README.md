# 数据库编程

## Python的DB-API

### 模块属性

#### DB-API 模块属性

属性|描述
----|---
apilevel|需要适配器兼容的 DB-API 版本
threadsafety|本模块的线程安全级别
paramstyle|本模块的 SQL 语句参数风格
connect()|Connect()函数

#### 数据库参数风格paramstyle

参数风格|描述|示例
-------|---|----
numeric|数值位置风格|WHERE name=:1
named|命名风格|WHER name=:name
pyformat|Python字典printf()格式转换|WHERE name=%(name)s
qmark|问号风格|WHERE name=?
format|ANSIC的printf格式转换|WHERE name=%s

#### connect()函数属性

参数|描述
----|---
user|用户名
password|密码
host|主机名
database|数据库名
dsn|数据源名

#### DB-API 异常类

异常|描述
----|---
Warning|警告异常基类
Error|错误异常基类
InterfaceError|数据库接口(非数据库)错误
DatabaseError|数据库错误
DataErro|处理数据时出现问题
OperationalError|数据库操作执行期间出现错误
IntegrityError|数据库关系完整性错误 
InternalError|数据库内部错误
ProgrammingError|SQL 命令执行失败
NotSupoortedError|出现不支持的操作

#### Connection对象方法

方法名|描述
-----|---
close()|关闭数据库连接
commit()|提交当前事务
rollback()|取消当前事务
cursor()|使用该连接创建(并返回)一个游标或类游标的对象
errorhandler(cxn, cur, errcls, errval)|作为给定连接的游标的处理程序

### Cursor对象

#### Cursor对象属性

对象属性|描述
-------|---
arraysize|使用 fetchmany()方法时，一次取出的结果行数，默认为 1 
connection|创建此游标的连接(可选)
description|返回游标活动状态(7 项元组):(name, type_code, display_size, internal_ size, precision, scale, null_ok)，只有 name 和 type_code 是必需的
lastrowid|上次修改行的行 ID(可选;如果不支持行 ID，则返回 None) 
rowcount|上次 execute*()方法处理或影响的行数
callproc( func [,args])|调用存储过程
close()|关闭游标
execute (op[,args])|执行数据库查询或命令
executemany (op，args)|类似 execute()和 map()的结合，为给定的所有参数准备并执行数据库查询 或命令
fetchone()|获取查询结果的下一行
fetchmany([size=cursor. arraysize])|获取查询结果的下面 size 行
fetchall()|获取查询结果的所有(剩余)行
__iter__()|为游标创建迭代器对象(可选，参考 next())
messages|游标执行后从数据库中获得的消息列表(元组集合，可选)
next ()|被迭代器用于获取查询结果的下一行(可选，类似 fetchone()，参考 __iter__())
nextset()|移动到下一个结果集合(如果支持) 
rownumber|当前结果集中游标的索引(以行为单位，从 0 开始，可选)  
setinputsizes(sizes)|设置允许的最大输入大小(必须有，但是实现是可选的)
setoutputsize(size[,col])|设置大列获取的最大缓冲区大小(必须有，但是实现是可选的)

#### 类型对象和构造函数

类型对象|描述
-------|---
Date (yr, mo, dy)|日期值对象
Time (hr, min, sec)|时间值对象
Timestamp (yr, mo, dy, hr, min, sec)|时间戳值对象
DateFromTicks (ticks)|日期对象，给出从新纪元时间(1970 年 1 月 1 日 00:00:00 UTC)以来的秒数 
TimeFromTicks (ticks)|时间对象，给出从新纪元时间(1970 年 1 月 1 日 00:00:00 UTC)以来的秒数 
TimestampFromTicks (ticks)|时间戳对象，给出从新纪元时间(1970 年 1 月 1 日 00:00:00 UTC)以来的秒数 
Binary (string)|对应二进制(长)字符串对象
STRING|表示基于字符串列的对象，比如 VARCHAR
BINARY|表示(长)二进制列的对象，比如 RAW、BLOB 
NUMBER|表示数值列的对象
DATETIME|表示日期/时间列的对象 
ROWID|表示“行 ID”列的对象

## 相关文档

#### 数据库相关模块/包及其网站

名称|在线参考文档
----|---------
关系数据库|
Gadfly|gadfly.sf.net
MySQL|mysql.com or mysql.org
MySQldb, 即MySQL-python|sf.net/projects/mysql-python
MySQL Connector/Python|launchpad.net/myconnpy
PostgreSQL|postgresql.org
psycopg|initd.org/psycopg
PyPgSQL|pypgsql.sf.net
PyGreSQL|pygresql.org
SQLite|sqlite.org
pysqlite|trac.edgewall.org/wiki/PySqlite
sqlite3|docs.python.org/library/sqlite3
APSW|code.google.com/p/apsw
MaxDB (SAP)|maxdb.sap.com 
sdb.dbapi|maxdb.sap.com/doc/7_7/46/702811f2042d87e10000000a1553f6/content.htm
sdb.sql|maxdb.sap.com/doc/7_7/46/702811f2042d87e10000000a1553f6/content.htm
sapdb|sapdb.org/sapdbPython.html
Firebird (InterBase)|firebirdsql.org
KInterbasDB|firebirdsql.org/en/python-driver
SQL Server|microsoft.com/sql
pymssql|code.google.com/p/pymssql(需要 FreeTDS[freetds.org])
adodbapi|adodbapi.sf.net
Sybase|sybase.com
sybase|www.object-craft.com.au/projects/sybase Oracle   oracle.com
cx_Oracle|cx-oracle.sf.net
DCOracle2|zope.org/Members/matt/dco2(已过时，仅支持 Oracle8)
Ingres|ingres.com
Ingres DBI|community.actian.com/wiki/Ingres_Python_Develop
ingmod|www.informatik.uni-rostock.de/~hme/software/ NoSQL 文档数据存储
NoSQL文档数据存储|
MongoDB|mongodb.org
PyMongo|pypi.python.org/pypi/pymong 文档:api.mongodb.org/python/current
PyMongo3|pypi.python.org/pypi/pymongo3
Other adapters|Other adapters api.mongodb.org/python/current/tools.html 
CouchDB|couchdb.apache.org
couchdb-python|code.google.com/p/couchdb-python 文档:packages.python.org/CouchDB
ORM|
SQLObject|sqlobject.org 
SQLObject2|sqlobject.org/2 
SQLAlchemy|sqlalchemy.org 
Storm|storm.canonical.com 
PyDO/PyDO2|skunkweb.sf.net/pydo.html

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
