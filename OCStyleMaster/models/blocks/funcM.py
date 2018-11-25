# -*- coding:utf-8 -*-

from OCStyleMaster.models.blocks.base.blockBase import *
import importlib


import re


class FuncM(BlockBase):



    def __init__(self, text):
        super(FuncM, self).__init__(text)
        self.type = Block.func
        self.bodyStart = 0
        self.bodyEnd = 0
        self._lineCount = -1
        self.funcHead = None
        self.funcBody = None



    def analyze(self):
        self.__get_func_head()
        self.__get_func_body()


        self.funcHead.analyze_by_config()
        self.funcBody.analyze_by_config()
        # self.__analyze_func_arg_count()
        self.__analyze_by_config()
        self.__analyze_body_line_count()


    def header_content(self):
        return self.content()[0:self.bodyStart]


    def __get_func_head(self):
        import OCStyleMaster.models.blocks.funcHead as FuncHead
        funcHead = FuncHead.FuncHead(self.text)
        funcHead.range = Range(start=self.range.start,end=self.bodyStart-1)
        funcHead.file = self.file
        self.funcHead = funcHead




    def __get_func_body(self):
        import OCStyleMaster.models.blocks.funcBody as FuncBody
        funcBody = FuncBody.FuncBody(self.text)
        funcBody.range = Range(start=self.range.start,end=self.range.end)
        funcBody.file = self.file
        self.funcBody = funcBody



    @classmethod
    def config_rule_names(cls):
        return []

    def line_count(self):
        if self._lineCount != -1:
            return self._lineCount

        regex = "\n"
        finds = re.findall(regex,self.content(),re.M)
        self._lineCount = len(finds)
        return self._lineCount


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
            err = self.create_error(self.range,ErrorType.suggest,"函数过长，超过50行",5)
            self.add_error_obj(err)
        elif 100 <= validLineCount:
            err = self.create_error(self.range, ErrorType.warn, "函数过长，超过100行",20)
            self.add_error_obj(err)



    def __analyze_by_config(self):
        self.analyze_by_config()


    # def __analyze_func_header(self):
    #     regex = "^[-+] \(" # 检查函数头，是否有一个空格
    #     m =  re.match(regex,self.content())
    #     if m is not None and m.pos == 0:
    #         return # OK
    #     else:
    #         err = self.create_error(self.range,ErrorType.warn,"函数头前空格个数错误")
    #         self.add_error_obj(err)


    # def __analyze_func_arg_count(self):
    #     regex = ":\("
    #     header = self.header_content()
    #     f = re.findall(regex,header)
    #     count = len(f)
    #     if count > 3:
    #         err = self.create_error(self.range,ErrorType.suggest,"参数过多")
    #         self.add_error_obj(err)
    #     pass

