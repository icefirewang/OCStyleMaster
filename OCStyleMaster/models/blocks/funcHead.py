# -*- coding:utf-8 -*-


from OCStyleMaster.models.blocks.base.blockBase import *
import re


class FuncHead(BlockBase):

    def __init__(self, text):
        super(FuncHead, self).__init__(text)
        self.type = Block.funcHead



    @classmethod
    def config_rule_names(cls):
        return ["funcHead"]