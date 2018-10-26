# -*- coding:utf-8 -*-

from .blockBase import *


class BigBracket(BlockBase):

    def __init__(self, text):
        super(BigBracket, self).__init__(text)
        self.type = Block.bigBracket



    @classmethod
    def start_text(cls):
        return "\{"

    @classmethod
    def end_text(cls):
        return "\}"

