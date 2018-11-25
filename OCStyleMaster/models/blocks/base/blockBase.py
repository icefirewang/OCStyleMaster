# -*- coding:utf-8 -*-

from OCStyleMaster.common import *
from OCStyleMaster.models.common import *
from OCStyleMaster.models.error import *
from OCStyleMaster.config import *
from OCStyleMaster.utils import *
from OCStyleMaster.globalData import *

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
    def config_rule_names(cls):
        return []

    def analyze_by_config(self):
        config =  GlobalData().config()
        defScore = config.defaultScore
        for name in self.__class__.config_rule_names():
            rules = config.get_rules(name)

            if rules is None:
                continue
            for r in rules:

                if "regex" not in r:
                    print("缺少 规则")
                    continue
                if "message" not in r:
                    print("缺少 错误信息")
                    continue

                regex = r["regex"]
                message = r["message"]
                max = 0 if not "max" in r else r["max"]  # 超过 max 才算有问题
                score = defScore if "score" not in r else r["score"]  #  应扣分数
                level = ErrorType.warn
                if "level" in r:
                    level = r["level"]
                    level = ErrorType(level)
                results = RegexUtil.full_search(regex, self.content())
                count = len(results)
                if count <= max:
                    continue
                for result in results:
                    start = self.range.start + result[0]
                    end = self.range.start + result[1]
                    range = Range(start,end)
                    err = self.create_error(range, level, message,score)
                    self.add_error_obj(err)
                    if max > 0:
                        break

    def check_func_comments(self):
        import OCStyleMaster.models.blocks.funcH as Func
        import OCStyleMaster.models.blocks.comment as Comment
        score = GlobalData().config().headerFileLackComment
        index = -1
        for c in self.children:
            index += 1
            if isinstance(c, Func.FuncH) == False:
                continue
            if index == 0:
                err = self.create_error(c.range, ErrorType.error, "函数缺少注释",score)
                self.add_error_obj(err)
                continue
            pre = self.children[index - 1]
            if isinstance(pre, Comment.Comment_N) == False:
                err = self.create_error(c.range, ErrorType.error, "函数缺少注释",score)
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


    def create_error(self,range,type,message,score=0):
        """
        创建一个 error
        :param offset:  fileOffset
        :param type:  类型
        :param message:  消息
        :return:
        """
        err = StyleError(self.file,range.start,range.end,type,message,score)
        return err


    def add_error_obj(self,err):
        """
        将错误，添加到file数组中
        :param err:
        :return:
        """
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