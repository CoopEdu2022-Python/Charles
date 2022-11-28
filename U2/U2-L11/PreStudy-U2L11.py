# 1. 什么是模块？
"""
|模块是Python 程序架构的一个核心概念
·每一个以扩展名py结尾的Python源代码文件都是一个模块
·模块名同样也是一个标识符，需要符合标识符的命名规则
·在模块中定义的全局变量、函数、类都是提供给外界直接使用的工具
·模块就好比是工具包，要想使用这个工具包中的工具，就需要先导入这个模块
"""
# 2. 如何导入模块？有哪些方式？
# 3. 不同的模块导入方式有什么区别？
"""
import 导入：
    import 模块名1, 模块名2  # 这个不推荐使用
    import 模块名1
    import 模块名2 as 模块别名  # 可以给新的模块换一个名字
    导入之后：
        通过模块名.使用模块提供的工具--全局变量、函数、类
from 模块名 import 导入：
    如果希望从某一个模块中，导入部工具，就可以使用from..import的方式
    import 模块名是一次性把模块中所有工具全部导入，并且通过模块名/别名访问
    from 模块名 import 工具名
    导入之后：
        不需要通过模块名.
        可以直接使用模块提供的工具--全局变量、函数、类
        如果两个模块，存在同名的函数，那么后导入模块的函数，会覆盖掉先导入的函数开发时
        import代码应该统一写在代码的顶部，更容易及时发现冲突一旦发现冲突，可以使用as关键字给其中一个工具起一个别名
from 模块名 import *：
    不推荐使用，因为函数重名没有提示，出现问题不好排查
"""

# 4. 导入模块时，模块的搜索顺序是怎样的？
"""
Python的解释器在导入模块时，会:
    1.搜索当前目录指定模块名的文件，如果有就直接导入
    2.如果没有，再搜索系统目录
在开发时，给文件起名，不要和系统的模块文件重名Python 中每一个模块都有一个内置属性file可以查看模块的完整路径
"""

