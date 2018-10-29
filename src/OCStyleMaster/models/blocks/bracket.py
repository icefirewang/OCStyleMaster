# -*- coding:utf-8 -*-

from .blockBase import *


class Bracket(BlockBase):


    def __init__(self,text):
        super(Bracket, self).__init__(text)
        self.type = Block.bracket


    @classmethod
    def start_text(cls):
        return "\("


    @classmethod
    def end_text(cls):
        return "\)"

