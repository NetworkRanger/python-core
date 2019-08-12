# 附录B 参考表

## Python关键字

#### Python关键字

关键字|关键字|关键字|关键字
-----|-----|-----|-----
and|as|assert|break
class|continue|def|del
elif|else|except|exec
finally|for|from|global
if|import|in|is
lambda|nonlocal|not|or
pass|print|raise|return
try|while|with|yield

## Python标准操作符和函数

#### 标准类型操作符和函数

操作符/函数|描述|结果
----------|---|---
字符串表示||
''|一种可以计算的字符串表示|str
内置和工厂函数||
cmp(obj1, obj2)|比较两个对象|int
repr(obj)|一种可以计算的字符串表示|str
str(obj)|可打印的字符串表示|str
type(obj)|对象类型|type
值比较||
<|小于|bool
>|大于|bool
<=|小于或等于|bool
>=|大于或等于|bool
==|等于|bool
!=|不等于|bool
<>|不等于|bool
对象比较||
is|相同于|bool
is not |不同于|bool
布尔操作符||
not|逻辑非|bool
and|逻辑与|bool
or|逻辑或|bool

## 数值类型操作符和函数

#### 所有数值类型操作符和内置函数

操作符/内置|描述|int|long|float|complex|结果
----------|---|---|----|-----|-------|---
abs()|绝对值|●|●|●|●|number
bin()|二进制字符串|●|●|●|●|str
chr()|字符|●|●| | |str
coerce()|数值强制转换|●|●|●|●|tuple
complex()|复杂工厂函数|●|●|●|●|complex
divmod()|除法/求模|●|●|●|●|tuple
float()|浮点型工厂函数|●|●|●|float
hex()|十六进制字符串|●|●| | |str
int()|int工厂函数|●|●|●|●|int
long()|long工厂函数|●|●|●|●|long
oct()|八进制字符串|●|●| | |str
ord()|序数||字符串| | |int
pow()|求幂|●|●|●|●|number
round()|浮点数取整| | |●| |float
sum()|求和|●|●|●| |float
**|求幂|●|●|●|●|number
+|没变化|●|●|●|●|number
-d|取负|●|●|●|●|number
~d|位反转|●|●| | |int/long
**|求幂|●|●|●|●|number
/|经典除法或真除法|●|●|●|●|number
//|向下除法|●|●|●|●|number
%|取模/求余数|●|●|●|●|number
+|加法|●|●|●|●|number
-|减法|●|●|●|●|number
<<|位左移|●|●| | |int/long
>>|位右移|●|●| | |int/long
&|按位与|●|●| | |int/long
^|按位异或|●|●| | |int/long
&#124;|按位或|●|●| | |int/long

## 序列类型操作符和函数

#### 序列类型操作符、函数和内置方法

操作符内置函数或方法|str|list|tuple
-----------------|---|-----|----
\[](创建表)| |●| 
()| | |●
""|●| |
append()| |●|
capitalize|●| | 
center|●| |
chr()|●| |
cmp()|●|●|●
count()|●|●
decode()|●| |
encode()|●| |
endswith()|●| |
expandtabs()| | 
extend()| |●|
find()|●| |
format()|●| |
hex()|●| 
index()|●|●|●
insert()| |●|
isalnum()|●| |
isalpha()|●| |
isdecimal()|●| |
isdigit()|●| |
islower()|●| |
isnumeric()|●| | 
isspace()|●| |
istitle()|●| |
isupper()|●| |
join()|●| | 
len()|●|●|●
list()|●|●|●
ljust()|●| |
lower()|●| |
lstrip()|●| |
max()|●|●|●
min()|●|●|●
oct()|●| | 
ord()|●|
partition()|●| |
pop()| |●|
raw_input()|●| |
remove()| |●|
replace()|●| |
repr()|●|●|●
reverse()| |●|
rfind()|●| |
rindex()|●| |
rjust()|●| |
rpartition()|●| |
rsplit()|●| |
rstrip()|●| |
sort()| |●|
split()|●| |
splitlines()|●| |
startswith()|●| |
str()|●|●|●
strip()|●| |
swapcase()|●| |
title()|●| |
translate()|●| |
tuple()|●|●|●
type()|●|●|●
upper()|●| | 
zfill()|●| |
.（属性)|●|●|●
\[](切片)|●|●|●
\[:]|●|●|●
*|●|●|●
%|●| | 
+|●|●|●
in|●|●|●
not in|●|●|●

## 字符串格式化操作符转换符号

#### 字符串格式化操作符转换符号

格式化符号|转换
---------|---
%c|字符(整数[ASCII 值]或长度为 1 的字符串)
%r|格式化之前通过 repr()进行字符串转换
%s|格式化之前通过 str()进行字符串转换
%d或%i|有符号十进制整数
%u|无符号十进制整数
%o|(无符号)八进制整数 
%x或%X|(无符号)十六进制整数(小写或大写字母)
%e或%E|指数符号(小写 e 或大写 E)
%f或%F|浮点实数(自动截断小数)
%g或%G|%e 和%f 或%E%和%F%的简短写法
%%|非转义的百分号字符(%)

## 字符串格式化操作符指令

#### 格式化操作符辅助指令

符号|功能
----|---
*|参数指定宽度或精度
−|使用左对齐
+|为正数使用加号(+)
<sp>|为正数使用空格填充
#|根据是否使用 x 或 X，添加八进制前导零(0)或十六进制前导 0x 或 0X
0|当格式化数字时使用零(而不是空格)填充
%|%%提供一个单符号%
(var)|映射变量(字典参数)
m.n|m 是最小总宽度，n 是小数点后面要显示的数字的位数(如果合适)

## 字符串类型内置方法

#### 字符串类型内置方法

方法名|描述
------|---
string.capitalize()|字符串的第一个字母大写
string.center(width)|返回一个共 width 列、填充空格的字符串，原始字符串处于其中心位置
string.count(str, beg=0, end=len(string))|统计 str 在 string 中出现的次数，如果给定了开始索引 beg 和结束索引 end， 将统计 str 在 string 的子串中出现的次数
string.decode(encoding='UTF-8, 'errors='strict')|返回 string 的解码字符串版本;如果发生错误，默认情况下会抛出一个 ValueError 异常，除非通过 ignore 或 replace 给出了 errors
string.encode(encoding='UTF-8', 'errors='strict ')|返回 string 的编码字符串版本;如果发生错误，默认情况下会抛出一个 ValueError 异常，除非通过 ignore 或 replace 给出了 errors
string.endswith(str, beg=0, end=len(string))|确定 string 或 string 的子串(如果给出了开始索引 beg 和结束索引 end)是否 以 str 结尾，如果是则返回 True，否则返回 False
string.expandtabs(tabsize=8)|在 string 中扩展制表符为多个空格;如果 tabsize 没提供，默认情况下每个制 表符为 8 个空格
string.find(str, beg=0, end=len(string))|确定 str 是否出现在 string 中;如果给定了开始索引 beg 和结束索引 end，则 会确定 str 是否出现在 string 的子串中;如果发现则返回索引，否则返回−1
string.format(*args, **kwargs)|根据传入的 args 和/或 kwargs 进行字符串格式化
string.index(str, beg=0, end=len(string))|与 find()相同，但如果未找到 str，则会抛出一个异常
string.isalnum()|如果 string 中至少含有 1 个字符并且所有字符都是字母数字，那么返回 True 否则返回 Fals
string.isalpha()|如果 string 中至少含有 1 个字符并且所有字符都是字母，那么返回 True 否则 返回 False
string.isdecimal()|如果 string 只包含十进制数则返回 True，否则返回 False 
string.isdigit()|如果 string 只包含数字则返回 True，否则返回 False
string.islower()|如果 string 包含至少 1 个区分大小写的字符并且所有区分大小写的字符都是小 写的，则返回 True，否则返回 False
string.isnumeric()|如果 string 只包含数字字符则返回 True 否则返回 False
string.isspace()|如果 string 只包含空格字符则返回 True 否则返回 False
string.istitle()|如果 string 是适当“标题大小写风格”(见 title())则返回 True，否则返回 False
string.isupper()|如果 string 包含至少 1 个区分大小写的字符并且所有区分大小写的字符都是大 写的，则返回 True，否则返回 False
string.join(seq)|将 seq 序列中的元素字符串表示合并(连接)到一个字符串，string 作为分隔符 
string.ljust(width)|返回一个空格填充的 string，原始字符串在总列数为 width 的空间中左对齐 
string.lower()|将 string 中所有的大写字母转换为小写字母
string.lstrip()|删除 string 中的所有前置空格
string.replace(str1, str2, num=string.count(str1))|用 str2 替换 string 中出现的所有 str1，或者最多 num 个(如果给定了 num) 
string.rfind(str, beg=0, end=len(string))|与 find ()相同，但在 string 中向后搜索
string.rindex( str, beg=0, end=len(string))|与 index()相同，但在 string 中向后搜索
string.rjust(width)|返回一个空格填充的 string，原始字符串在总列数为 width 的空间中右对齐 
string.rstrip()|删除 string 中所有的尾部空格
string.split(str="", num=string.count(str))|根据分隔符 str(如果没提供，默认为空格)分割 string 并返回子串的列表; 如果给定了 num，则最多分为 num 个子串
string.splitlines(num=string.count('\n'))|在所有(或 num 个)换行处分割 string 并返回一个删除换行符后每行的列表
string.startswith(str, beg=0, end=len(string))|确定 string 或其子串(如果给定了开始索引 beg 和结束索引 end)是否以子串
str 开始，若是则返回 True，否则返回 False
string.strip([obj])|对 string 执行 lstrip()和 rstrip()操作
string.swapcase()|反转 string 中所有字母大小写
string.title()|返回 string 的“标题大小写风格”版本，即所有单词都以大写字母开始，而其 余字母小写(另外参见 istitle())
string.translate(str, del="")|根据翻译表 str(256 个字符)翻译 string，并删除 del 字符串中的内容 
string.upper()|将 string 中的小写字母转换为大写字母
string.zfill(width)|返回左填充 0 并且总字符数为 width 的原始字符串;用于数字，zfill()保留任 何给定的符号(少一个 0)
   
   
## 列表类型内置方法

#### 列表类型内置方法

列表方法|操作
-------|---
list.append(obj)|将 obj 添加到 list 末尾
list.count(obj)|返回 obj 在 list 中出现的次数
list.extend(seq)|将 seq 的内容附加到 list 中
list.index(obj,i=0,j=len(list))|返回使 list[k]==obj 和 i≤=k<j 同时成立的最小索引 k，否则抛出 ValueError 异常
list.insert()|将 obj 插入 list 中的偏移量 index 处
list.pop()|从 list 中删除并返回在给定或最后索引处的 obj
list.remove(obj)|从 list 中删除对象 obj
list.reverse()|按顺序反转 list 中的对象
list.sort(func=None, key=None, reverse=None)|利用可选的比较函数 func 排序列表成员;当提取要排序的元素时 key 是一个回调，并且如果 reverse 标记为 True，则 list 将以倒序排序

## 字典类型内置方法

#### 字典类型方法

方法名|操作
-----|---
dict.clear()|删除 dict 中的所有元素
dict.copy()|返回 dict 的一份(浅)2拷贝
dict.fromkeys(seq, val=None)|创建并返回一个新字典，其中 seq 的元素作为字典的键，val 作为所有键对应的 初始值(若没给定，则默认为 None)
dict.get(key, default=None)|对于键key返回其对应的值，或者若dict中不含key则返回default(注意，default 的默认值为 None)
dict.has_key(key)|如果 key 存在于 dict 中则返回 True，否则返回 False;在 Python2.2 中被 in 和 not in 操作符部分替代，但是仍旧提供一个功能接口
dict.items()|返回 dict 的(key, value)元组对的一个迭代版本
dict.iter()|iteritems()、iterkeys()、itervalues()都是行为与它们的非迭代器版本相同的方法， 但是返回一个迭代器，而不是一个列表
dict.keys()|返回 dict 所有键的一个迭代版本
dict.pop(key[,default])|类似于 get()，但删除并返回 dict[key](如果给定了 key);如果 key 不存在于 dict
dict.setdefault(key, default=None)|中且未给出 default，则抛出 KeyError 异常
dic.update(dict2)|类似于 get()，但如果 key 不存在于 dict 中，则设置 dict[key]=default 将 dict2 中的键值对添加到 dict 中
dict.values()|返回 dict 中值的一个迭代版本

## 集合类型操作符和内置函数

#### 集合类型操作符、函数和内置方法

函数/方法名|等效操作符|描述
----------|--------|---
所有集合类型|
len(s)| |集合基数: s中元素的数量
set([obj])| |可变集合工厂函数；如果给出了obj，那么它必须是可迭代的，并且新的元素取自obj；如果没有给出，则创建一个空集合
frozenset([obj])| |不可改变的工厂函数；除了返回不可改变的集合之外，其他动作方式与set()相同
frozenset([obj])|obj in s|成员测试：obj是s的一个元素吗
frozenset([obj])|obj not in s|非成员测试：obj不是s的一个元素吗
frozenset([obj])|s == t|等价测试：s和t拥有完全相同的元素吗
frozenset([obj])|s != t|不等价测试：与==相反
frozenset([obj])|s < t|（严格的）子集测试：s != t 且s的所有元素都是t的成员
s.issubset(t)|s <= t|子集测试（允许不适当的子集）：s的所有元素都是t的成员
s.issubset(t)|s > t|（严格的）超集测试：s != t 用t的所有元素都是s的成员
s.issuperset(t)|s >= t|超集测试（允许不适当的超集）：t所有的元素都是s的成员
s.union(t)|s&#124;t|并操作：s或t中的元素
s.intersection(t)|s-t|差操作：存在于s中且不存在于t中的元素。
s.systemric_difference(t)|s^t|对称差操作：仅仅存在于s和t二者之一中的元素
s.copy()| |复制操作：返回s的（浅）复制
s.update(t)|s&#124;=t|(联合）更新操作：把t中成员添加到s中
s.intersection_update(t)|s&=t|交更新操作：s仅仅包含原始s与t的成员
s.difference_update(t)|s-=t|差更新操作：s仅仅包含s中不存在于t中的原始成员
s.systemtric_difference_update(t)|s^=t|对称差更新操作：s只包含原始s和t二者之一中的成员
s.add(obj)| |添加操作：将obj添加到s中
s.remove(obj)| |删除操作：从s中删除obj；如果obj不存在于s中，则抛出KeyError异常
s.discard(obj)| |丢弃操作：remove()的更友好版本，如果obj存在于s中，则从s中移除obj
s.pop()| |弹出操作：删除并返回s中的任意元素
s.clear()| |清除操作：删除s的所有元素

## 文件对象方法和数据属性

## 文件对象方法

文件对象属性|描述
----------|---
file.close()|关闭 file
file.fileno()|返回 file 的整数文件描述符
file.flush()|冲刷 file 的内部缓冲器
file.isatty()|如果 file 是一个类 tty 设备，则返回 True;否则返回 False
file.next()|返回 file 中的下一行(类似 file.readline())，或如果没有更多行则抛出 StopIteration 异常
file.read(size=1)|读取文件中的 size 个字节，如果 size 未给出或为负数，则读取所有剩余的字节，作为一个字符串 返回
file.reainto(buf,size)|从 file 中读取 size 个字节到缓冲器 buf 中(不支持)
file.readline(size=1)|从 file 中读取并返回一行(包括行结束字符)，为一整行或 size 字符的最大值
file.readlins(sizhint=0)|从 file 中读取所有行并作为一个列表(包括所有行终止符)返回;如果给定了 sizhint 并且 sizhint > 0，则返回由大约 sizhint 个字节(可以向上圆整到下一个缓冲器的值)组成的整个行
file.xreadlines()|用于迭代，返回 file 中的行，它作为块以一种比 readlines()更有效的方式读取
file.seek(off, whence=0)|移动到 file 中的某个位置，从 whence 的 off 字节的偏移量处(0 表示文件的开始，1 表示当前位置，2 表示文件末尾)
file.tell()|返回 file 内的当前位置
file.truncate(size=file.tell())|以最多 size 字节来截断 file，默认为当前文件位置
file.write(str)|向 file 中写入字符串 str
file.writeline(seq)|将字符串 seq 写入 file 中;seq 应该是一个可迭代产生的字符串;在 Python 2.2 版本之前，它仅仅 是一个字符串列表
file.closed|如果 file 关闭了则为 True;否则为 False
file.encoding|这个文件使用的编码，当向 file 中写入 Unicode 字符串时，使用 file.encoding 将它们转换为字节字符串;值 None 表示应该使用系统默认的编码方式来转换 Unicode 字符串
file.mode|打开 file 的访问模式
file.name|file 名称
file.newlines|如果没有读取到行分隔符则为 None，否则为一个由一种类型的行分隔符组成的字符串，或一个包含当前读取的行终止符所有类型的元组
file.softspace|如果 print 明确要求空格则为 0，否则为 1;很少供程序员使用，通常只供内部使用

## Python异常

#### Python内置异常

异常名称|描述
-------|---
BaseException|所有异常的基类
SystemExit|Python 解释器请求终止
KeyboardInterrupt|用户中断执行(通常通过按 Ctrl + C 组合键)
Exception|常用异常的基类
StopIteration|迭代没有更多值
GeneratorExit|发送到生成器令其停止的异常
SystemExit|Python 解释器请求终止 所有标准内置异常的基类
ArithmeticError|所有数值计算错误的基类
FloatingPointError|浮点计中的错误
OverflowError|计算结果超出数值类型最大限制 
ZeroDivisionError|被零除(或求模)错误(所有数值类型)
AssertionError|assert 声明失败 
AttributeError没有这种对象属性
EOFError|没有从内置输入就到达了文件末尾标志
EnvironmentError|操作系统环境错误的基类
IOError|输入/输出操作失败
OSError|操作系统错误
WindowsError|MS Windows 系统调用失败
ImportError|导入模块或对象失败
KeyboardInterrupt|用户中断执行(通常通过按 Ctrl + C 组合键)
LookupError|无效数据查找错误的基类
IndexError|序列中没有这种索引
KeyError|映射中没有这个键
MemoryError|内存不足错误(对 Python 解释器来说非致命)
NameError|未声明/未初始化的对象(非属性)
UnboundLocalError|访问一个未初始化的局部变量
ReferenceError|弱引用试图访问一个垃圾回收的对象
RuntimeError|执行过程中的通用默认错误
NotImplementedError|未实现的方法
SyntaxError|Python 语法错误
IndentationError|不适当的缩进
TabError|不当的制表符和空格
SystemError|通用解释器系统错误
TypeError|类型的无效操作
ValueError|给定了无效参数
UnicodeError|Unicode 相关错误 
UnicodeDecodeError解码过程中的 Unicode 错误
UnicodeEncodeError|编码过程中的 Unicode 错误
UnicodeTranslateError|转换过程中的 Unicode 错误
Warning|所有警告的基类
DeprecationWarning|弃用特性的警告
FutureWarning|警告在未来将会改变语义的结构
OverflowWarning|自动长时间升级的旧警告
PendingDeprecationWarning|与未来将会弃用的特性相关的警告
RuntimeWarning|可疑运行时行为相关的警告
SysntaxWarning|可疑语法相关的警告
UserWarning|用户代码产生的警告

## 类的特殊方法  
  
#### 自定义类的特殊方法

特殊方法|描述
-------|---
基本自定义|
C.__init__(self, [arg1, ...])|构造函数(附带任何可选参数) 
C.__new__(self, [arg1, ....])|构造函数(附带任何可选参数);通常用于创建不可变数据类型的子类 
C.__del__(self)|析构函数
C.__str__(self)|可打印字符串表示;str()内置方法和 print 语句 
C.__repr__(self)|可计算字符串表示;repr()内置方法和′′操作符
C.__unicode__(self)|Unicode 字符串表示;repr()内置方法和‘ ’操作符
C.__call__(self)|表示可调用的实例
C.__nonzero__(self)|为对象定义 False 值;bool()内置方法(自版本 2.2 起)
C.__len__(self)|“Length”(适用于类);len()内置方法
对象（值）比较|
C.__cmp__(self,obj)|对象比较;cmp()内置方法 
C.__lt__(self,obj)和C.__le__(self,obj)|小于/小于或等于;<和<=操作符 
C.__gt__(self,obj)和C.__ge__(self,obj)|大于/大于或等于;>和>=操作符 
C.__eq__(self,obj)和C.__ne__(self,obj)|等于/不等于;==、!=和<>操作符
属性|
C.__attr__(self, attr)|获取属性;getattr()内置方法
C.__setattr__(self, attr, val)|设置属性；setattr()内置方法
C.__delattr__(self, attr)|删除属性；del语句
C.__getattribute__(self, attr)|获取属性；getattr()内置方法
C.__set__(self, attr, val)|设置属性；setattr()内置方法
C.__delete__(self, attr)|删除属性；del语句
自定义类/模拟类型|
数据类型：二进制操作符|
C.__*add__(self, obj)|加法；+操作符
C.__*sub__(self, obj)|减法；-操作符
C.__*mul__(self, obj)|乘法；*操作符
C.__*div__(self, obj)|除法；/操作符
C.__*truediv__(self, obj|真除法；/操作符
C.__*floordiv__(self, obj)|向下除法；//操作符
C.__*mod__(self, obj)|模/余数；%操作符
C.__*divmod__(self, obj)|除法和模运算；divmod()内置方法
C.__*pow__(self, obj[, mod])|求幂；pow()内置方法；**操作符
C.__*lshift__(self, obj)|左移；<<操作符
C.__*rshift__(self, obj)|右移；>>操作符
C.__*and__(self, obj)|位与；&操作符
C.__*or__(self, obj)|位或；&#124;操作符
C.__*xor__(self, obj)|位异或；^操作符
数值类型：一元操作符|
C.__neg__(self)|一元非
C.__pos__(self)|一元无变化
数值类型：一元操作符|
C.__abs__(self)|绝对值；abs()内置方法
C.__invert(self)|位倒置；~操作符
数值类型：数值转换|
C.__complex__(self,com)|转换成复数；complex()内置方法
C.__init__(self)|转换成int类型；int()内置方法
C.__long__(self)|转换成long类型；long()内置方法
C.__float__(self)|转换成float；float()内置方法
数值类型：基础表示（字符串）|
C.__oct__(self)|八进制表示；oct()内置方法
C.__hex__(self)|十六进制表示;hex()内置方法
数据类型：数值强制转换|
C.__coerce__(self, num)|强制转换为相同的数据类型；coerce()内置方法
序列类型|
C.__len__(self)|序列中条目的数量
C.__getitem__(self, ind)|得到单个序列元素
C.__setitem__(self, ind, val)|设置单个序列元素
C.__delitem__(self, ind)|删除单个序列元素
C.__getslice__(self, ind1, ind2)|获取序列切片
C.__setslice__(self, i1, i2, val)|设置序列切片
C.__delslice__(self, ind1, ind2)|删除序列切片
C.__contains__(self, val)|测试序列成员;in 关键字
C.__*add__(self, obj)|连接;+操作符
C.__*mul__(self, obj)|复制;*操作符
C.__iter__(self)|创建迭代器类;iter()内置方法
映射类型|
C.__len__(self)|散列中条目的数量
C.__hash__(self)|散列函数值
C.__getitem__(self, key)|用给定键获取对应的值
C.__setitem__(self, key, val)|用给定键设置对应的值
C.__delitem__(self, key)|用给定键删除对应的值

## Python操作符汇总

#### Python操作符（一元的）

Operator|int|long|float|complex|str|list|tuple|dict|set,frozenset
--------|---|----|-----|-------|---|----|-----|----|-------------
\[]| | | | |●|●|●| |
\[:]| | | | |●|●|●| |
**|●|●|●|●| | | | |
+|●|●|●|●| | | | |
-|●|●|●|●| | | | |
~|●|●| | | | | | |
*|●|●|●|●|●|●|●| |
/|●|●|●|●| | | | |
//|●|●|●|●| | | | |
%|●|●|●|●|●| | | | 
+|●|●|●|●|●|●|●| |
-|●|●|●|●| | | | |●
<<|●|●| | | | | |
>>|●|●| | | | | |
&|●|●| | | | | | |●
^|●|●| | | | | | |●
&#124;|●|●| | | | | | |●
<|●|●|●|●|●|●|●|●|●
>|●|●|●|●|●|●|●|●|●
<=|●|●|●|●|●|●|●|●|●
>=|●|●|●|●|●|●|●|●|●
==|●|●|●|●|●|●|●|●|●
!=|●|●|●|●|●|●|●|●|●
<>|●|●|●|●|●|●|●|●|●
is|●|●|●|●|●|●|●|●|●
is not|●|●|●|●|●|●|●|●|●
in| | | | |●|●|●| |●
not in| | | | |●|●|●| |●
not|●|●|●|●|●|●|●|●|●
and|●|●|●|●|●|●|●|●|●
or|●|●|●|●|●|●|●|●|●


