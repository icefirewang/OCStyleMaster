# -*- coding:utf-8 -*-

from OCStyleMaster.models.blocks.base.blockBase import *
import os
from OCStyleMaster.globalData import *



class File(BlockBase):

    def __init__(self, filePath):
        f = open(filePath, "r")
        text = f.read()
        f.close()
        super(File, self).__init__(text)
        self.path = filePath
        _, ext = os.path.splitext(self.path)
        self.ext = ext
        self.filename = os.path.basename(self.path)
        self.file = self
        self.type = Block.file
        self.range = Range(0,len(self.text))
        self.lineCount = 0
        self.linePoses = self.__get_line_poses()
        self.errors = []    # 错误
        self.deduction = 0  # 减分


    def analyze(self):
        """
        分析主函数
        :return:
        """
        for child in self.children:
            child.analyze()



    # def __analyze_line(self):
    #     lines = self.content().split("\n")
    #     index = 0
    #     for line in lines:
    #         length = len(line)
    #         if 80 < length and length <= 100:
    #             err = StyleError(index+1, 1, ErrorType.suggest, "行过长，超过80字节")
    #             self.add_error_obj(err)
    #         elif length > 100:
    #             err = StyleError(index+1, 1, ErrorType.warn, "行过长，超过100字节")
    #             self.add_error_obj(err)
    #         else:
    #             pass
    #         index+=1

    def __get_line_poses(self):
        start = 0
        ret = []
        while True:
            pos = self.text.find("\n",start)
            if pos < 0:
                break
            ret.append(pos)
            start = pos+1
        return ret


    def line_pos(self,pos):
        """
        将文件位置，转化位 行数，和行位置数
        从 0 行 0 列还开
        :param pos:
        :return:
        """
        linePoses = self.linePoses
        index = 0
        for p in linePoses:
            if p >= pos:
                break
            index+=1
        linePos = 0
        lineCount = 0
        if index > 0:
            linePos = linePoses[index-1]
            lineCount = index

        poslinePos = pos-linePos
        return lineCount,poslinePos


    def ext(self):
        """
        后缀
        :return:
        """
        return self.ext


    def output_all_errors(self):
        """
        输出 错误
        :return:
        """
        score = 100
        errors = sorted(self.errors,key = lambda obj:obj.start)

        print("[{}]".format(self.filename))
        for e in errors:
            print(e)
            score = score - e.score

        print("得分 {}".format(score))

