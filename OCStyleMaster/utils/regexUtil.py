# -*- coding:utf-8 -*-


import re
class RegexUtil:

    @staticmethod
    def find_all_func_declare(text):
        regex = "\n\s?[-+]\s*\(.*\)[A-z_]+[A-z0-9_]*[^\{]*{"
        return re.findall(regex,text,re.M)


    @staticmethod
    def find_all_if_unit(text):
        regex = "if\(.*\)"
        return re.findall(regex, text)


    @staticmethod
    def find_all_elif_unit(text):
        regex = "else +if\(.*\)"
        return re.findall(regex, text)


    @staticmethod
    def line_count(text):
        regex = "\n"
        ret = re.findall(regex,text)
        return len(ret)


    @staticmethod
    def is_comment_line(text):
        regex = "\s*//.*"
        m = re.search(regex,text)
        if m is not None and m.span(0)[0]==0:
            return True
        else:
            return False

    @staticmethod
    def empty_line_count(text):
        regex = "\n\n"
        ret = re.findall(regex,text)
        return len(ret)

    @staticmethod
    def full_search(regex,text):
        ret = []
        temp = text
        pos = 0
        while True:
            m = re.search(regex,temp,re.M)
            if m is None:
                break
            start = m.span()[0]
            end = m.span()[1]
            realStart = pos+start
            realEnd = pos+end
            temp = temp[end:]
            ret.append((realStart,realEnd))
            pos+=end
        return ret


