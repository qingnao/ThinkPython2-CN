def linecount(filename):
    count = 0
    for line in filename:
        count += 1
    return count

# 通常，当你导入一个模块，只应定义新的函数，而不应该执行它们。
# 如果需要将程序作为模块导入，通常遵循下面的写法：
if __name__ == '__main__':  
    print(linecount('wc.py'))

# __name__是一个内置变量，程序运行便被赋值，当作脚本运行时就是 '__main__'。
# 如果是作为模块被导入，就不是main了，测试代码也就不用执行。
