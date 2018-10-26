# -*- coding:utf-8 -*-

from .blockBase import *


class MidBracket(BlockBase):

    def __init__(self, text):
        super(MidBracket, self).__init__(text)
        self.type = Block.midBracket



    @classmethod
    def start_text(cls):
        return "\["


    @classmethod
    def end_text(cls):
        return "\]"