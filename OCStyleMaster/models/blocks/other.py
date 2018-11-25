# -*- coding:utf-8 -*-
from OCStyleMaster.models.blocks.base.blockBase import *


class Other(BlockBase):

    def __init__(self, text):
        super(Other, self).__init__(text)
        self.type = Block.other
