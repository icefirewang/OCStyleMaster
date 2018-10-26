# -*- coding:utf-8 -*-


g_config = None
import json
import re
from common import *
from globalData import *
from json.decoder import  JSONDecodeError
import configparser
class Config:

    def __init__(self):
        self.config = {}
        self.init_config()


    def permissive_json_loads(self,text):
        while True:
            try:
                data = json.loads(text)
            except JSONDecodeError as exc:
                if exc.msg == "Invalid \\escape":
                    text = text[:exc.pos] + "\\"+text[exc.pos:]
                else:
                    raise
            else:
                return data

    def __func_header_config(self):
        ret = []
        return ret

    def __rules_func_h(self):
        ret = [
            {
                "regex": "[^ ]+\*",
                "message": "*号前缺少空格"
            }
        ]
        return ret

    def __rules_property(self):
        ret = [
            {
                "regex":".*strong.*NSString.*",
                "message":"NSString 要用 copy 不能用 strong",
                "type":ErrorType.error
            }
        ]
        return ret

    def __rules_func_m(self):
        func = [
            {
                "regex": "[^ ]+\*",
                "message": "*号前缺少空格"
            },
            {
                "regex": ".*==[^ ]+",
                "message": "==后缺少空格"
            },
            {
                "regex": "[^ ]+==",
                "message": "==前缺少空格"
            },
            {
                "regex": "[^= ]+=[^=]*",
                "message": "=号前缺少空格"
            },
            {
                "regex": "[^=]=[^ =]+",
                "message": "=号后缺少空格"
            },
            {
                "regex": "objectAtIndex:",
                "message": "不要直接使用 objectAtIndex"
            },
            {
                "regex":" addObject:[^@]+.*]",
                "message": "不要直接使用 addObject"
            },
            {
                "regex":" setObject:[^@].* forKey:.*\]",
                "message": "不要直接使用 setObject: forKey:"
            },
            {
                "regex": " setObject:.* forKey:[^@].*\]",
                "message": "不要直接使用 setObject: forKey:"
            },
            {
                "regex":"[A-z_]+[A-z0-1_]*\[.*\] \s*=\s* [^@].*",
                "message": "不要直接使用 dict[key] = value"
            },
            {
                "regex": "[A-z_]+[A-z0-1_]*\[[^@].*\] \s*=\s* .*",
                "message": "不要直接使用 dict[key] = value"
            },
            {
                "regex": ".*\s*=\s*.*[A-z_]+[A-z0-1_]*\[.*\]",
                "message":"不要直接使用 array[index] 如果是 C 数组，请忽略"
            },
            {
                "regex":"removeObjectForKey:",
                "message":"不要直接使用 removeObjectForKey"
            }

        ]
        return func


    def init_config(self):

        self.config = {
            "funcM":self.__rules_func_m(),
            "property":self.__rules_property(),
            "funcH":self.__rules_func_h()
        }



    def init_config2(self):
        try:
            path = GlobalData().configPath
            f = open(path,"r")
            text = f.read()
            f.close()
            configs = self.permissive_json_loads(text)
            for block in configs:
                listConfig = configs[block]
                for unit in listConfig:
                    regex = unit["regex"]
                    # regex = regex.replace("@",r"\%")
                    # regex = regex.replace("%","")
                    unit["regex"] = regex
                    print(regex)
            print("load config {}".format(configs))
            self.config = configs
        except Exception as e:
            print(e)



    def get_rules(self,type):
        """
        获取 对应的种类规则
        :param type:
        :return:
        """
        regexs = self.config[type]
        return regexs



def instance():
    global g_config
    if g_config is None:
        g_config = Config()

    return g_config
