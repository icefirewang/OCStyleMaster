# -*- coding:utf-8 -*-

import os
import subprocess

path = __file__

version = "0.2.3"


def parent_path(path):
    return os.path.split(path)[0]


setupTemplate = os.path.join(parent_path(path),"setup_template")
root =  parent_path(parent_path(path))
setupFile = os.path.join(root,"setup.py")
destPath = root


def create_real_setup_file(templatePath,realPath):
    f = open(templatePath,"r")
    text = f.read()
    f.close()
    text = text.replace("__VERSION__",version)

    f = open(realPath,"w+")
    f.write(text)
    f.close()

create_real_setup_file(setupTemplate,setupFile)

tarFile = os.path.join(root,"dist","ocstylemaster-{}.tar.gz".format(version))



cmds = [
    "cd {} && python3 {} sdist".format(destPath,setupFile),
    "which python",
    "twine upload {}".format(tarFile)
]


for cmd in cmds:
    print("exe cmd:>> {}".format(cmd))
    os.system(cmd)