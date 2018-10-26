# -*- coding:utf-8 -*-

from common import *
from models import *





class BlockAnalyzerH:

    def __init__(self,block,analyzePos):
        self.block = block
        self.text = block.text
        self.length = 0
        self.pos = analyzePos



    def start(self):
        # self.__clean_text()
        self.__prepare()
        self.__analzye()



    def __prepare(self):
        self.length = len(self.text)




    def __analzye(self):
        self.__normal_analyze()


    def __valid_blocks(self):
        ret = [
            Property,
            InterfaceH,
            Comment_N,
            Comment_1,
            Protocol,
            FuncH,
        ]
        return ret


    def __find_start(self,buffer,pos):
        find = self.__is_include_start_text(buffer)
        if find is None:
            return pos
        m = find[0]
        cls = find[1]
        # print("find child {}".format(cls))
        # 分析 block
        span = m.span(0)
        len = m.end(0) - m.start(0) - 1
        start = pos - len
        block = self.__create_block(cls, self.text, start)
        block.file = self.block.file
        block.parent = self.block
        analyzer = BlockAnalyzerH(block,block.range.start+1)
        analyzer.start()
        self.block.add_child(block)
        end = analyzer.block.range.end
        if end == 0:
            raise Exception("block no end {}".format(analyzer.block))
        pos = end + 1
        return pos


    def __normal_analyze(self):
        buffer = ""
        pos = self.pos
        while pos < self.length:
            # print("post {}".format(pos))
            c = self.text[pos]
            buffer = buffer + c
            # print("buffer {}".format(buffer))
            # 找Block头
            if self.block.type != Block.comment_1 and self.block.type != Block.comment_n:
                newPos = self.__find_start(buffer,pos)
                if newPos != pos:
                    pos = newPos
                    buffer = ""
                    continue

            # 找block 尾部
            index = self.__is_include_end_text(buffer)
            if index >= 0:
                self.block.range.end = pos
                # print("find end {} pos {}".format(self.block.type,pos))
                break
            pos += 1



    def __is_include_start_text(self,text):
        blockClasses = self.__valid_blocks()
        for cls in blockClasses:
            start = cls.start_text()
            if start is None:
                continue
            m = re.search(start,text,re.M)
            if m is not None:
                ret = (m,cls)
                return ret
        return None


    def __is_include_end_text(self,text):
        cls = type(self.block)
        try:
            endText = cls.end_text()
            if endText is None:
                return -1
            m  = re.search(endText,text,re.M)
            if m is None:
                return -1
            return m.pos
        except :
            print(cls)



    def __create_block(self,type,text,start):
        ret  = type(text)
        ret.range.start = start
        return ret

