# -*- coding:utf-8 -*-


class BlockUtil:


    @classmethod
    def get_block_end_pos(cls,text,start,end,startPos=0):
        """
        获取一个BLOCK的开始点和结束点
        :param text:  文本
        :param start:  开始 字符，如『{』
        :param end: 结束字符，如『}』
        :param startPos:  开始查找的位置
        :return:  结束的位置，找不到 返回None
        """
        buffer = ""
        pos = startPos
        same = 0
        blockStartPos = None
        blockEndPos = None
        while(pos < len(text)):
            buffer += text[pos]
            newStart = buffer.rfind(start)
            # 找到开始符号
            if newStart >= 0:
                buffer = ""
                same += 1
                if blockStartPos is None:
                    blockStartPos = pos

            endPos =  buffer.rfind(end)
            # 找到结束符号
            if endPos >= 0:
                buffer = ""
                assert (same > 0)
                same -= 1
                if same == 0:
                    blockEndPos = pos
                    break
            pos+=1
        return blockStartPos,blockEndPos

