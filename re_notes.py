#coding:utf-8
#author:andong
#删除注释规则
import os
import re
import shutil

frompath = r"/Users/xudongan/rules/rules3"

files = os.listdir(frompath)
for filename in files:





    with open(frompath+'/'+filename,'r') as f:
        with open('/Users/xudongan/rules/rules3/emerging-attack_response02.rules','w') as g:
            for line in f.readlines():
                if '#alert' not in line:
                    g.write(line)
    shutil.move('/Users/xudongan/rules/rules3/emerging-attack_response02.rules',frompath+'/'+filename)





