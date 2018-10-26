# -*- coding:utf-8 -*-

from .blockBase import *

import re
from utils import *


class FuncH(BlockBase):

    def __init__(self, text):
        super(FuncH, self).__init__(text)
        self.type = Block.func


    @classmethod
    def config_rule_names(cls):
        return ["funcH"]

    @classmethod
    def start_text(cls):
        regex = "[-+]\s*\([\w\*]*\)[A-z_]+[A-z0-9_\s\*\(\): ]*;"
        return regex

    @classmethod
    def end_text(cls):
        regex = ";"
        return regex

    def analyze(self):
        self.analyze_by_config()
        self.__analyze_func_arg_count()


    def __analyze_func_arg_count(self):
        regex = ":\("
        header = self.content()
        f = re.findall(regex,header)
        count = len(f)
        if count > 3:
            err = self.create_error(self.range.start,ErrorType.suggest,"参数过多")
            self.add_error_obj(err)
        pass

