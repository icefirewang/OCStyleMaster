# -*- coding:utf-8 -*-



"""
level 0 : suggest
level 1 : warn
level 3 : error
"""

g_config = None # 单例用


class Config:

    def __init__(self):
        self.config = {}
        self.__init_config()




    def __init_config(self):
        """
        初始化配置
        :return:
        """
        self.config = {
            "funcM": self.__rules_func_m(),
            "property": self.__rules_property(),
            "funcH": self.__rules_func_h(),
            "funcDeclare":self.__func_declare_config()
        }


    def __func_declare_config(self):
        """
        函数声明的正则规则
        :return:
        """
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
        """
        属性声明的规则配置
        :return:
        """
        ret = [
            {
                "regex":".*strong.*NSString.*",
                "message":"NSString 要用 copy 不能用 strong",
                "level":3
            }
        ]
        return ret

    def __rules_func_m(self):
        """
        .m 文件内的 函数的 正则表达式
        :return:
        """
        func = [
            {
                "regex":"\{[\s]*\}",
                "message":"逻辑分支内为空，请加入 do nothing 注释"
            },
            {
                "regex":"[^ \n]\{",
                "message":"{ 前缺少空格"
            },
            {
                "regex": "[^ ]\*",
                "message": "*号前缺少空格"
            },
            {
                "regex": ".==[^ ]",
                "message": "==后缺少空格"
            },
            {
                "regex": "[^ ]+==",
                "message": "==前缺少空格"
            },
            {
                "regex": "[^= ]+=[^=]",
                "message": "=号前缺少空格"
            },
            {
                "regex": "[^=]=[^ =]",
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




    def get_rules(self,type):
        """
        获取 对应的种类规则
        :param type:
        :return:
        """
        ret = self.config[type]
        return ret



def instance():
    """
    单例函数
    :return: 返回 配置的单例
    """
    global g_config
    if g_config is None:
        g_config = Config()
    return g_config
