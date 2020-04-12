# -*- coding:utf-8 -*-
"""
@author: Biscuit@Linux
https://github.com/BiscuitAtLinux/pyPhotoRenamer
"""

from __future__ import print_function
import os
import sys
from DateName import DateName

basedir = '.'
#第一个参数，照片目录，默认为当期目录
if len(sys.argv)>1:
    basedir = sys.argv[1]

#第二个参数，序号位数，默认为3
if len(sys.argv)>2:
    DateName.serialLength = sys.argv[2]

#第三个参数，起始编号，默认为1
if len(sys.argv)>3:
    DateName.serialNumber = int(sys.argv[3])

#切换工作目录
os.chdir(basedir)

#basedir下所有文件
filenames = []

for parent,dirnames,files in os.walk('.'):
    if parent == '.':
        for file in files:
            filenames.append(file)

#按文件名排序
filenames.sort()

#存储上一次遍历的文件名，同样主文件名不同后缀的文件只读取一次
lastName = ""

#存储时间、文件名信息
dateNames = []

#遍历所有文件
for filename in filenames:
    splitName = filename.split('.')
    name = splitName[0]
    #同样主文件名不同后缀的文件只读取一次
    if name == lastName:
        continue
    ext = splitName[len(splitName)-1].lower()
    #只处理支持的图形文件
    if ext in ['jpg','arw','cr2','tif','tiff','rw2','dng','raf']:
        lastName = name
        dateNames.append(DateName(filename))

#遍历并改名
for i in range(0,len(dateNames)):
    oldName = dateNames[i].name
    if i == 0:
        newName = dateNames[i].getNewName()
    else:
        newName = dateNames[i].getNewName(dateNames[i-1])
    print(oldName, 'to', newName)
    #修改各种支持的后缀
    for ext in ['JPG','ARW','CR2','TIF','TIFF','jpg','arw','cr2','tif','tiff','RW2','rw2','DNG','dng','RAF','raf']:
        try:
            os.rename(oldName+'.'+ext,newName+'.'+ext)
        except:
            pass
