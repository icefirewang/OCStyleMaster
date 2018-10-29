# -*- coding:utf-8 -*-
import os
path = __file__
projectPath = os.path.dirname(path)
os.chdir(projectPath)

import argparse
import traceback
from OCStyleMaster.tools import *
from OCStyleMaster.models import *
from OCStyleMaster.utils import *



def analyze_m_file(path):
    file = FileM(path)
    blockAnalyzer = BlockAnalyzerM(file,0)
    blockAnalyzer.start()
    file.analyze()
    file.print_all_errors()


def analyze_h_file(path):
    file = FileH(path)
    blockAnalyzer = BlockAnalyzerH(file, 0)
    blockAnalyzer.start()
    file.analyze()
    file.print_all_errors()



def analyze_folder(path):
    for dirpath,dirnames,filenames in os.walk(path):
        for name in filenames:
            path = dirpath + "/"+name
            try:
                analyze_path(path)
            except Exception as e:
                print("file error {}".format(path))
                print(e)
                traceback.print_exc()


def analyze_path(path):
    extension = Util.extension(path)
    print("file path {}".format(path))
    if extension == ".m":
        analyze_m_file(path)
    elif extension == ".h":
        analyze_h_file(path)
    elif extension == "":
        analyze_folder(path)
    else:
        pass
        # print("ignore file : {} ".format(path))

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file","-f",help="要分析的文件，或文件夹，文件必须是 .m 或 .h 文件")
    args = parser.parse_args()

    filePath = args.file
    analyze_path(filePath)
    print("end")











if __name__ == '__main__':
    main()