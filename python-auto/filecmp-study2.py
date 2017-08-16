#!/usr/bin/env python
# -*- coding:utf-8 -*-
#校验源与备份目录的差异

import os , sys
import filecmp
import re
import shutil
from _ast import Compare


holderlist = []
def compareme(dir1,dir2):    #递归获取更新项目函数
    dircomp = filecmp.dircmp(dir1,dir2)
    only_in_one = dircomp.left_only   #源目录存在的文件或是目录
    diff_in_one = dircomp.diff_files  #不匹配文件，源目录文件已经发生改变
    dirpath = os.path.abspath(dir1)   #定义源目录的绝对路径
    print dirpath
    
    #将更新的文件名或是目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_in_one]
    if len(dircomp.common_dirs) > 0:  #判断是否有相同的目录，方便递归
        for item in dircomp.common_dirs:  #递归子目录
            compareme(os.path.abspath(os.path.join(dir1,item)), os.path.abspath(os.path.join(dir2,item)))
            return holderlist
    
    
def main():
    if len(sys.argv) > 2:   #要求输入源目录和备份目录
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print "Usage:" ,sys.argv[0],"datadir backupdir"
        sys.exit()
        
    source_files = compareme(dir1, dir2)  #对比与目录和备份目录
    dir1=os.path.abspath(dir1)
    
    if not dir2.endswith('/'):           #在需要备份的目录后面添加‘/’符号
        dir2 = dir2+'/'
    dir2 = os.path.abspath(dir2)
    destination_files = []
    createdir_bool = False
    
    for item in source_files:            #遍历返回的差异文件和目录
        destination_dir=re.sub(dir1, dir2, item)  #将源目录的差异路径清单备份到备份目录
        
        destination_files.append(destination_dir)
        if os.path.isdir(item):   #如果差异路径不存在需要在备份目录中创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool = True
                
    if createdir_bool:
        destination_files = []
        source_files = []
        source_files = compareme(dir1, dir2)  #再次调用目录文件差异函数
        for item in source_files:
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)
            
    
    print "update item:"
    print source_files
    copy_pair = zip(source_files,destination_files)
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])
        
if __name__ == "__main__":
    main()
            
        
    