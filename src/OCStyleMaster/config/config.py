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
        self.defaultScore = 0.5




    def __init_config(self):
        """
        初始化配置
        :return:
        """
        self.config = {
            # "funcH": self.rules_func_h(),
            "funcBody": self.rules_func_body(),
            "property": self.rules_property(),
            "funcDeclare":self.func_declare_config(),
            "funcHead":self.rules_func_header()
        }


    def func_declare_config(self):
        """
        函数声明的正则规则
        :return:
        """
        ret = []
        return ret

    def rules_func_h(self):
        ret = [
            {
                "regex": "[^ ]+\*",
                "message": "*号前缺少空格",
                "score":0.5
            }
        ]
        return ret

    def rules_property(self):
        """
        属性声明的规则配置
        :return:
        """
        ret = [
            {
                "regex":".*strong.*NSString.*",
                "message":"NSString 要用 copy 不能用 strong",
                "level":3,
                "score":5,
            }
        ]
        return ret

    def rules_func_header(self):
        """
        函数头规则
        :return: rule
        """
        ret = [
            {
                "regex":"(^[-+]\()|(^[-+] {2:}\()",
                "message":"函数头前空格个数错误"
            },
            {
                "regex" : ":\(",
                "message":"函数参数过多",
                "max" : 3,
            }
        ]
        return ret

    def rules_func_body(self):
        """
        .m 文件内的 函数的 正则表达式
        :return:
        """
        func = [
            {
                "regex":"\{[\s]*\}",
                "message":"逻辑分支内为空，请加入 do nothing 注释",
                "score":1,
            },
            {
                "regex":"[^ \n]\{",
                "message":"{ 前缺少空格",
                "score":0.5
            },
            {
                "regex": "[^ ]\*",
                "message": "*号前缺少空格",
            },
            {
                "regex": ".==[^ ]",
                "message": "==后缺少空格",
            },
            {
                "regex": "[^ ]+==",
                "message": "==前缺少空格",
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
                "message": "不要直接使用 objectAtIndex",
                "score":"3",
            },
            {
                "regex":" addObject:[^@]+.*]",
                "message": "不要直接使用 addObject",
                "score":"3"
            },
            {
                "regex":" setObject:[^@].* forKey:.*\]",
                "message": "不要直接使用 setObject: forKey:",
                "score": "3"
            },
            {
                "regex": " setObject:.* forKey:[^@].*\]",
                "message": "不要直接使用 setObject: forKey:",
                "score": "3"
            },
            {
                "regex":"[A-z_]+[A-z0-1_]*\[.*\] \s*=\s* [^@].*",
                "message": "不要直接使用 dict[key] = value",
                "score": "3"
            },
            {
                "regex": "[A-z_]+[A-z0-1_]*\[[^@].*\] \s*=\s* .*",
                "message": "不要直接使用 dict[key] = value",
                "score": "3"
            },
            {
                "regex": ".*\s*=\s*.*[A-z_]+[A-z0-1_]*\[.*\]",
                "message":"不要直接使用 array[index] 如果是 C 数组，请忽略",
                "score": "3"
            },
            {
                "regex":"removeObjectForKey:",
                "message":"不要直接使用 removeObjectForKey",
                "score": "3"
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
