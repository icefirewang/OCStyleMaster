# -*- coding:utf-8 -*-

from .blockBase import *
from utils import *
from .funcM import *


class Implement(BlockBase):

    def __init__(self, text):
        super(Implement, self).__init__(text)
        self.type = Block.implement
        self.funcCount = 0



    def analyze(self):
        self.__get_all_funcs()
        self.__analyze_pragma_mark_count()
        for child in self.children:
            child.analyze()



    def __analyze_pragma_mark_count(self):
        """
        分析函数个数，并查看那是否有足够的pragma mark 宏分开
        :return:
        """
        regex = "\n#pragma mark"
        regex = re.compile(regex)
        finds = regex.findall(self.content())
        markCount = len(finds)
        needCount = int(self.funcCount/5)-1
        if markCount < needCount:
            err = self.create_error(self.range.start,ErrorType.suggest,"是否没有足够的program mark宏将函数分组")
            self.add_error_obj(err)




    def __get_all_funcs(self):
        content = self.content()
        regex = "\n[-+]\s*\(.*\)[A-z_]+[A-z0-9_]*[^\{]*{"
        ranges = RegexUtil.full_search(regex,content)
        self.funcCount = len(ranges)
        for r in ranges:
            start = r[0]+1
            end = r[1]
            bodyStart,bodyEnd = BlockUtil.get_block_end_pos(content,"{","}",start)
            func = FuncM(self.text)
            func.bodyStart = self.range.start + bodyStart
            func.bodyEnd = self.range.start + bodyEnd
            func.parent = self
            func.range.start = self.range.start + start
            func.range.end = self.range.start + bodyEnd
            func.parent = self
            func.file = self.file
            self.add_child(func)


    def __get_all_funcs2(self):
        content = self.content()
        funHeaders = RegexUtil.find_all_func_declare(content)
        print(funHeaders)
        self.funcCount = len(funHeaders)
        for header in funHeaders:
            if header[0] == "\n":
                header = header[1:-1]
            pos = content.find(header)
            assert (pos>=0)
            start ,end = BlockUtil.get_block_end_pos(content,"{","}",pos)
            func = FuncM(self.text)
            func.bodyStart = start
            func.bodyEnd = end
            func.parent = self
            func.range.start = self.range.start + pos
            func.range.end = self.range.start + end
            func.parent = self
            func.file = self.file
            self.add_child(func)




    @classmethod
    def start_text(cls):
        return "@implementation"

    @classmethod
    def end_text(cls):
        return "@end"


