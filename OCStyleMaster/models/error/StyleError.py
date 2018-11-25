# -*- coding:utf-8 -*-

from OCStyleMaster.common import *

class StyleError:
    def __init__(self,file,start,end,type,message,score = 0 ):
        self.type = type
        self._line = None
        self._linePos = None
        self.message = message
        self.file = file
        self.start = start
        self.end = end
        score = float(score)
        self.score = score



    def line_number(self):
        """
        获取行号 0 开始
        :return:
        """
        if self._line is None:
            assert (self.file is not None)
            self._line , self._linePos  = self.file.line_pos(self.start)

        return self._line

    def line_pos(self):
        """
        获取行位置 0开始
        :return:
        """
        if self._linePos is None:
            assert (self.file is not None)
            self._line, self._linePos = self.file.line_pos(self.start)

        return self._linePos

    def __str__(self):
        startLine = self.line_number() + 1
        startLinePos = self.line_pos()

        # endLine = self.file.line_pos(self.end)[0] + 1
        # endLinePos = self.file.line_pos(self.end)[1]
        error_string = self.error_string(self.type)
        ret = "{} => POS [{}:{}] : {}  -{}".format(error_string,startLine,startLinePos,self.message,self.score)
        return ret


    def error_string(self,type):
        if type == ErrorType.suggest:
            return "SUGGEST"
        if type == ErrorType.error:
            return "ERROR"
        if type == ErrorType.warn:
            return "WARN"
        return "Unknown"