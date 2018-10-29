# -*- coding:utf-8 -*-
from enum import Enum

class Block(Enum):
    bracket = 1
    midBracket = 2  # 中括号
    bigBracket = 3  # 大括号
    func = 4        # 函数 声明
    property = 6    # 变量声明
    interface = 7 # 类的 interface
    implement = 8 # 类的实现
    file = 9    # 文件
    macro = 10   # 宏
    comment_1 = 11 # 注释 但行
    comment_n = 12 # 注释 多行
    other = 13 # 其它
    protocol = 14

class AnalyzeType(Enum):
    line = 0 # 行
    block = 1 # 块
    mfile = 2 # .m 文件
    hfile = 3 # .h 文佳

class ErrorType(Enum):
    error = "error"
    warn = "warn"
    suggest = "suggest"