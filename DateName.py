# -*- coding:utf-8 -*-
__author__ = 'Biscuit@Linux'

import pyexiv2

class DateName:
    """
    存储照片的拍摄日期及文件名信息
    """

    #初始化文件序列号（类变量）
    serialNumber = 1
    #编号位数（类变量）
    serialLength = 3

    def __init__(self, filename):
        """
        构造函数
        :param filename: 原文件名
        :return:
        """

        #解析EXIF信息
        matedata = pyexiv2.ImageMetadata(filename)
        matedata.read()
        photoDate = matedata['Exif.Photo.DateTimeOriginal'].value

        #初始化实例变量，年月日
        self.year = photoDate.year
        self.month = photoDate.month
        self.day = photoDate.day
        #原文件名
        self.filename = filename
        splitName =filename.split('.')
        #主文件名
        self.name = splitName[0]
        #后缀
        self.ext = splitName[len(splitName)-1]

    def getNewName(self,lastDateName = None):
        """
        得到新的主文件名
        :param lastDateName: DateName列表中的上一个对象
        :return:
        """

        #如果年月日都相同，或者是第一次调用，则继续编号
        if lastDateName is not None and self.year == lastDateName.year\
                and self.month == lastDateName.month and self.day == lastDateName.day\
                or lastDateName is None:
            pass
        #如果不同，则重置编号为1
        else:
            DateName.serialNumber = 1
        newName = self._getName()
        #编号自增
        DateName.serialNumber+=1
        return newName

    def _getName(self):
        """
        按照 yyyyMMdd-nnn 的格式生成新的主文件名
        :return:
        """
        return ("%4d%02d%02d-%0"+str(DateName.serialLength)+"d")%(self.year,self.month,self.day,DateName.serialNumber)