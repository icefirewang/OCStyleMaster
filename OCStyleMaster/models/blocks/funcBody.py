# -*- coding:utf-8 -*-


from OCStyleMaster.models.blocks.base.blockBase import *
import re


class FuncBody(BlockBase):

    def __init__(self, text):
        super(FuncBody, self).__init__(text)
        self.type = Block.funcBody



    @classmethod
    def config_rule_names(cls):
        return ["funcBody"]