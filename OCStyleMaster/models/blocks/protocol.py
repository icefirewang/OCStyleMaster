# -*- coding:utf-8 -*-

from .blockBase import *
from utils import *
from .property import *

class Protocol(BlockBase):

    def __init__(self, text):
        super(Protocol, self).__init__(text)
        self.type = Block.protocol




    def analyze(self):
        self.check_func_comments()
        for child in self.children:
            child.analyze()
        pass



    @classmethod
    def start_text(cls):
        return "@protocol[^;]*\n"

    @classmethod
    def end_text(cls):
        return "@end"