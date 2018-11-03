# -*- coding:utf-8 -*-

from OCStyleMaster.models.blocks.base.blockBase import *


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

