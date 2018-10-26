# -*- coding:utf-8 -*-

from .blockBase import *

import re
from utils import *


class FuncM(BlockBase):

    def __init__(self, text):
        super(FuncM, self).__init__(text)
        self.type = Block.func
        self.bodyStart = 0
        self.bodyEnd = 0
        self._lineCount = -1



    def analyze(self):
        self.__analyze_func_header()
        self.__analyze_func_arg_count()
        self.__analyze_by_config()
        self.__analyze_body_line_count()


    def header_content(self):
        return self.content()[0:self.bodyStart]


    # def __analyze_line(self):
    #     lines = self.content().split("\n")
    #     index = -1
    #     for line in lines:
    #         index += 1
    #         if RegexUtil.is_comment_line(line):
    #             continue
    #         length = len(line)
    #         if length > 120:
    #             err = StyleError(index+1, 1, ErrorType.warn, "行过长，超过120字节")
    #             self.add_error_obj(err)
    #         else:
    #             pass

    @classmethod
    def config_rule_names(cls):
        return ["funcM"]

    def line_count(self):
        if self._lineCount != -1:
            return self._lineCount

        regex = "\n"
        finds = re.findall(regex,self.content(),re.M)
        self._lineCount = len(finds)
        return self._lineCount


    @classmethod
    def start_text(cls):
        return ""

    def __analyze_body_line_count(self):
        regex = "\n[ \f\n\r\t\v]*\n{1,}"
        regex = re.compile(regex)
        finds = regex.findall(self.content())
        subCount = 0
        for f in finds:
            nCount = len(re.findall("\n",f))-1
            subCount += nCount
        validLineCount = self.line_count() - subCount
        if 50 < validLineCount  and  validLineCount < 100:
            err = self.create_error(self.range.start,ErrorType.suggest,"函数过长，超过60行")
            self.add_error_obj(err)
        elif 100 <= validLineCount:
            err = self.create_error(self.range.start, ErrorType.warn, "函数过长，超过100行")
            self.add_error_obj(err)



    def __analyze_by_config(self):
        self.analyze_by_config()


    def __analyze_func_header(self):
        regex = "^[-+] \(" # 检查函数头，是否有一个空格
        m =  re.match(regex,self.content())
        if m is not None and m.pos == 0:
            return # OK
        else:
            err = self.create_error(self.range.start,ErrorType.warn,"函数头前空格个数错误")
            self.add_error_obj(err)


    def __analyze_func_arg_count(self):
        regex = ":\("
        header = self.header_content()
        f = re.findall(regex,header)
        count = len(f)
        if count > 3:
            err = self.create_error(self.range.start,ErrorType.suggest,"参数过多")
            self.add_error_obj(err)
        pass

