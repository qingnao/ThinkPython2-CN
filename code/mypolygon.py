import turtle
import math

bob = turtle.Turtle()
print(bob)

# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)

# turtle.mainloop()

# tuetle模块提供了函数 Turtle，可以用来创建 Tuttle 对象，我们将其分配给名为 bob 的变量。
# 输出 bob 会显示如下类似信息：
# <turtle.Turtle object at 0x102e96510>
# 这意味着 bob 指向了一个类型为 Turtle 的对象，该对象是在模块 turtle 中定义的。
# 一旦创建了 Turtle 对象，便可以调用方法在窗口中移动它，方法和函数蕾丝，但略有不同。
# 调用bob的fd方法就是前进。forward lt rt就是转向。
# 这不就是类似的扫地机器人吗？任何一个交通工具都是这样设计的，向前直行，可以调转方向。

# 习题后面有答案，因此在完成（或至少尝试）之前，先不要查看。

# 1. 编写 square 函数，参数是个 turtle 对象 t，用 turtle 绘制正方形。
# 编写一个函数调用，将 bob 作为参数传给 square，然后运行程序。

# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)

# square(bob)
# turtle.mainloop()



# 2. 为 square 添加参数 length，修改函数体，令边的长度为 length，同时修改函数
# 令其调用第二个实参，再次运行程序，使用不同的值测试 length 的范围。

# def square(t, length):
#     """用小乌龟进行前进或调转方向
#     t: turtle对象，是小乌龟
#     length: 边的长度
#     """
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)

# square(bob, 80)

# turtle.mainloop()

# 3. 复制 square 并命名为 polygon. 添加另一个参数n，并修改函数，令其绘制正n边形
# 提示，正n边行外角角度为 360/n度。

# def polygon(t, n, length):
#     """用小乌龟进行前进或调转方向
#     t: turtle对象，是小乌龟
#     length: 边的长度
#     n: 绘制图形的边数
#     """
#     angle = 360/n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# polygon(bob, 10, 36)
# turtle.mainloop()

# 4. 编写 circle 函数，以 turtle类型的 t，以及半径 r 为参数，通过使用适当长度和边数，来调用polygon函数，
# 绘制一个近似的圆，用不同的 r 值，测试程序。提示：确定圆的周长，使其满足边长 * 边数 = 周长。

# def circle(t, r):
#     """绘制一个近似的圆
    
#     t: turtle 小乌龟进程
#     r: 半径
#     """
#     # polygon里的长度和边数都是根据r来计算的，所以获取的值会传递给它
    
#     # 圆的周长可以通过公式 L=2πr, 其中L是圆的周长，r是圆的半径，π是一个常数，可以用math.pi来获取
    
#     # 如果r=5，那么周长L是多少？
#     # 如果边数n设置为6 那么长度是多少？
#     n = 100
#     l = 2 * r * math.pi
#     # 圆的周长=边长 * 边数，边数=n
#     length = l/n

    
#     polygon(t, length, n)

# circle(bob, 50)

# 5. 升级 circle 版本，命名为 arc，新增参数 angle， 用此值确定所绘制的圆弧的大小。
# angle以度为单位，当 angle=360，arc会绘制一个完整的圆。

def arc(t, r, angle):
    """绘制一个近似的圆
    
    t: turtle 小乌龟进程
    r: 半径
    """
    # polygon里的长度和边数都是根据r来计算的，所以获取的值会传递给它
    
    # 圆的周长可以通过公式 L=2πr, 其中L是圆的周长，r是圆的半径，π是一个常数，可以用math.pi来获取
    
    # 如果r=5，那么周长L是多少？
    # 如果边数n设置为6 那么长度是多少？
    n = 100
    l = 2 * r * math.pi
    # 圆的周长=边长 * 边数，边数=n
    length = l/n

    
    polygon(t, length, n)

# arc(bob, 50)

# 4.4 封装 
# 将一段代码写在函数中，叫做封装。封装的好处之一在于，用一个简单的名字来指代一段代码，类似文档说明。
# 另一个好处是可以复用代码，调用函数两次总比复制粘贴大段的代码要更简洁！

# 4.5 泛化
# 当函数有多个数值参数时，很容易混淆各自代表什么，或者参数顺序。这种情况下，可以在传递实参列表时，附上形参的名字
# 这也叫做关键字参数，因为是把形参的名字作为“关键字”包含进来。
# 这种语法令程序可读性更强。同时也提示了实参和形参的工作原理：调用函数时，实参赋值给了形参。

# 4.6 接口设计 

# 编写circle，此函数以半径 r 为参数，以下是采用 polygon 来绘制正五十边形的简单解决方案
def circle(t, r):
    circumference = 2* math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n=n, length=length)

# 函数接口是函数用途的摘要：参数是什么？函数做什么？返回什么？如果一个接口允许调用者执行所需操作，
# 而无需处理无关的细节，那么这个接口就是简洁的。

# 与其将n作为参数传入令接口复杂，不如根据周长来确定一个合适的 n：
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)
# circle(bob, 50)

# 4.7 重构

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n ,length):
    angle = 360.0 / n
    polyline(t, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1    
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

circle(bob, 50)    

# 此过程---调整代码，优化接口，便于复用---叫做重构。
# 此案例中，我们发现 arc 和 polygon 具有一些相似代码，所以将其“抽离”为polyline。

# 如果早有规划，我们可能会优先编写 polyline，避免后续耗时重构，但一般你很难在项目开始的时候，
# 便深入了解一切，规划好所有接口。只有开始编码，你才会更好地研究并理解其中曲折。
# 所以，有时候重构便是你学到了一些东西的标志。

# 4.8 开发计划
# 尽量复制粘贴，减少打字（以及重复调试）
# 尝试重构程序。比如，在多个地方有相似代码，试试能否将其拆解为恰当的通用函数。

# 4.9 帮助文档

# 简要概括函数的功能（不涉及如何操作），并解释各个参数的类型和作用。

# 设计接口，重要的一步，便是编写友好的帮助文档。一个设计优良的接口，应该是易于理解的；
# 如果需要耗费大量口舌讲解，那么这个接口还有待改进。

# 4.11 术语表

# 封装: 将一系列语句转化为函数定义的过程。
# 泛化：将过于具体内容（比如数字）替换为通用内容(变量或参数)的过程
