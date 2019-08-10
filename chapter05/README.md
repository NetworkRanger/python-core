# GUI编程

## Tkinter和Python编程

### Tk控件

#### Tk 控件

控件|描述
----|--- 
Button|与 Label 类似，但提供额外的功能，如鼠标悬浮、按下、释放以及键盘活动/事件
Canvas|提供绘制形状的功能(线段、椭圆、多边形、矩形)，可以包含图像或位图
Checkbutton|一组选框，可以勾选其中的任意个(与 HTML 的 checkbox 输入类似) 
Entry|单行文本框，用于收集键盘输入(与 HTML 的文本输入类似)
Frame|包含其他控件的纯容器
Label|用于包含文本或图像
LabelFrame|标签和框架的组合，拥有额外的标签属性
Listbox|给用户显示一个选项列表来进行选择
Menu|按下 Menubutton 后弹出的选项列表，用户可以从中选择
Menubutton|用于包含菜单(下拉、级联等)
Message|消息。与 Label 类似，不过可以显示成多行
PanedWindow|一个可以控制其他控件在其中摆放的容器控件
Radiobutton| 一组按钮，其中只有一个可以“按下”(与 HTML 的 radio 输入类似)
Scale|线性“滑块”控件，根据已设定的起始值和终止值，给出当前设定的精确值 Scrollbar
Scrollbar|为 Text、Canvas、Listbox、Enter 等支持的控件提供滚动功能
Spinbox|Entry 和 Button 的组合，允许对值进行调整 多行文本框
Text|用于收集(或显示)用户输入的文本(与 HTML 的 textarea 类似) 
Toplevel|与 Frame 类似，不过它提供了一个单独的窗口容器

## 相关模块和其他GUI

#### Python中可用的GUI系统

GUI库|描述
-----|---
Tk相关模块|
Tkinter/tkinter|TK INTERface:Python 默认的工具包 http://wiki.python.org/moin/TkInter
Pmw|Python MegaWidgets(Tkinter 扩展) http://pmw.sf.net
Tix|Tk Interface eXtension(Tk 扩展) http://tix.sf.net
Tile/Ttk|Tile/Ttk 主题控件集 http://tktable.sf.net
TkZinc(Zinc)|扩展的 Tk 画布类型(Tk 扩展) http://www.tkzinc.org
EasyGUI(easygui)|非常简单且无事件驱动的 GUI(Tkinter 扩展) http://ferg.org/easygui
TIDE+(IDE Studio)|Tix 集成开发环境(包含 IDE Studio 和一个增强的 Tix 标准 IDLE IDE) http://starship.python.net/crew/mike
 WxWidgets相关模块|
 wxPython|wxWidgets 对 Python 的绑定版本，跨平台的 GUI 框架(过去名为 wxWindows) http://wxpython.org
Boa Constructor|Python IDE 和 wxPython GUI 构建工具 http://boa-constructor.sf.net
PythonCard|基于 wxPython 的桌面应用 GUI 构建工具包(受 HyperCard 启发) http://pythoncard.sf.net
wxGLade|另一个 wxPython GUI 设计工具(受 Glade、GTK+/GNOME GUI 构建工具启发) http://wxglade.sf.net
GTK+GNOME相关模块|
PyGTK|GIMP 工具包(GTK+)的 Python 封装库 http://pygtk.org
GNOME-Python|GNOME 桌面和开发库对 Python 的绑定版本 http://gnome.org/start/unstable/bindings http://download.gnome.org/sources/gnome-python
Glade|用于 GTK+和 GNOME 的 GUI 构建工具 http://glade.gnome.org
PyGUI(GUI)|跨平台的“Pythonic”式 GUI API(构建于 Cocoa [Mac OS X]和 GTK+[POSIX/X11 和 Win32]之上) http://www.cosc.canterbury.ac.nz/~greg/python_gui
QT/KDE相关模块|
PyQt|Trolltech 开发的 Qt GUI/XML/SQL C++工具包对 Python 的绑定版本(部分开源 [双重许可]) http://riverbankcomputing.co.uk/pyqt
PyKDE|KDE 桌面环境对 Python 的绑定版本 http://riverbankcomputing.co.uk/pykde
eric|PyQt 开发的使用 QScintilla 编辑器控件的 Python IDE http://die-offenbachs.de/detlev/eric3 http://ericide.python-hosting.com/
PyQtGPL|Qt(Win32Cygwin 端口)、Sip、QScintilla、PyQt 包 http://pythonqt.vanrietpaap.nl
其他开源GUI工具包|
FXPy|FOX 工具包(http://fox-toolkit.org)对 Python 的绑定版本 http://fxpy.sf.net
PyFLTK(fltk)|FLTK 工具包(http://fltk.org)对 Python 的绑定版本 http://pyfltk.sf.net
PyOpenGL(OpenGL)|OpenGL(http://opengl.org)对 Python 的绑定版本 http://pyopengl.sf.net
商业软件|
win32gui|微软 MFC(基于 Python 的 Windows 扩展) http://starship.python.net/crew/mhammond/win32
swing|Sun Microsystems Java/Swing(基于 Jython) http://jython.org
 
 
  
          
      
      
      
