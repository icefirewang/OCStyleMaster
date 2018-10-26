# -*- coding:utf-8 -*-

from common import *
from models.common import *
from models.error import *
from config import *
from utils import *
class BlockBase:

    def __init__(self,text,file=None):
        self.text = text
        self.children = []
        self.type = 0
        self.range = Range()
        self.parent = None
        self.file = file

        self._content = None


    def content(self):
        if self._content is not None:
            return self._content
        self._content = self.text[self.range.start:self.range.end+1]
        return self._content


    def add_child(self,child):
        self.children.append(child)
        # print("add_child  {}".format(child))


    def analyze(self):
        pass

    @classmethod
    def config_rule_names(cls,self):
        return []

    def analyze_by_config(self):
        for name in self.__class__.config_rule_names():
            rules = config().get_rules(name)
            if rules is None:
                continue
            for r in rules:
                regex = r["regex"]
                message = r["message"]
                type = ErrorType.warn
                if "type" in r:
                    type = r["type"]
                results = RegexUtil.full_search(regex, self.content())
                for r in results:
                    pos = self.range.start + r[0]
                    err = self.create_error(pos, type, message)
                    self.add_error_obj(err)

    def check_func_comments(self):
        import models.blocks.funcH as Func
        import models.blocks.comment as Comment
        index = -1
        for c in self.children:
            index += 1
            if isinstance(c, Func.FuncH) == False:
                continue
            if index == 0:
                err = self.create_error(c.range.start, ErrorType.error, "函数缺少注释")
                self.add_error_obj(err)
                continue
            pre = self.children[index - 1]
            if isinstance(pre, Comment.Comment_N) == False:
                err = self.create_error(c.range.start, ErrorType.error, "函数缺少注释")
                self.add_error_obj(err)
                continue

    def line_pos(self,pos):
        """
        将文件位置，转化位 行数，和格子数
        :param pos:
        :return:
        """
        linePoses = self.file.linePoses
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


    @classmethod
    def include_begin(cls,text):
        return None


    def create_error(self,pos,type,message):
        line, linePos = self.line_pos(pos)
        line += 1
        err = StyleError(line, linePos, type, message)
        return err


    def add_error_obj(self,err):
        self.file.errors.append(err)


    def __str__(self):
        start = self.line_pos(self.range.start)
        end = self.line_pos(self.range.end)
        ret = "{} : ({}:{})\n".format(self.type,start,end)
        ret += self.content()
        # for c in self.children:
        #     ret+=str(c)
        return ret



    @classmethod
    def start_text(cls):
        return None

    @classmethod
    def end_text(cls):
        return None