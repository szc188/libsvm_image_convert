# coding=utf-8

import os
import shutil
from PIL import Image
import numpy as np
import sys

work_dir = "train_images"

# try:
#     work_dir = sys.argv[1]
# except:
#     print('用法:\ttrain_img_cov.py [路径]')
#     exit(1)

class ImageTrainFileMake(object):
    def __init__(self, work_dir, width, height):
        self.work_dir = work_dir
        self.class_count = 0
        self.class_list = []
        self.file_count = 0
        self.width = width
        self.height = height
        self.train_str = ''
    
    # 将图片转换为训练字符串
    def img_to_str(self, image):
        count = 1
        img_str = ''
        for item in image.getdata():
            img_str = img_str + '%d' % count + ':' + '%d' % item + ' '
            count = count + 1
        return img_str
        
    # 将图片快速重采样  3x3的格子 取四角和中心点的平均
    def img_resample(self, image):
        img = Image.new("L", (int(image.width / 3), int(image.height / 3)))
        for h in range(0, int(image.height / 3)):
            for w in range(0, int(image.width / 3)):
                t0 = image.getpixel((h * 3, w * 3))
                t1 = image.getpixel((h * 3, w * 3 + 2))
                t2 = image.getpixel((h * 3 + 1, w * 3 + 1))
                t3 = image.getpixel((h * 3 + 2, w * 3))
                t4 = image.getpixel((h * 3 + 2, w * 3 + 2))
                t = (t0 + t1 + t2 + t3 + t4) / 5
                img.putpixel((w, h), (int(t)))
        return img

    # 读取图片
    def read_img(self, class_name, file_name, file_path):
        # try:
        #     file_path.index('.JPG')
        # except:
        #     return
        
        try:
            image = Image.open(file_path)
            print('train_img_cov: 类[%d]: %s  读取图片: %s' % (self.class_count, class_name, file_name))
            if image.width != self.width or image.height != self.size_y:
                print('train_img_cov: 图片尺寸不匹配(%d x %d)，调整大小' % (image.width, image.height))
                image = image.resize(size=(self.width, self.height))
            image = image.convert('L')
            image = self.img_resample(image)
            str = '%s ' % self.class_count + self.img_to_str(image) + '\n'
            self.train_str = self.train_str + str
            self.file_count = self.file_count + 1
        # print(str)
        except:
            pass

    # 遍历文件
    def iterate_file(self, class_name, dir_path):
        for parent, _, filenames in os.walk(dir_path):
            for filename in filenames:
                file_path = os.path.join(parent, filename)
                self.read_img(class_name, filename, file_path)

    # 遍历文件夹(类)
    def iterate_dir(self):
        for parent, dirnames, _ in os.walk(self.work_dir):
            for dirname in dirnames:
                dir_path = os.path.join(parent, dirname)
                print('train_img_cov: 展开文件夹: %s' % (dirname))
                self.class_list.append(dirname)
                self.iterate_file(dirname, dir_path)
                self.class_count = self.class_count + 1

    # 输出类对应的数字数组
    def output_class_table(self):
        count = 0
        print('#######################################')
        print('char *class_str[] = {')
        print('  ', end='')
        for item in self.class_list:
            print('"%s", ' % item, end='')
            count = count + 1
            if count == 4:
                count = 0
                print('')
                print('  ', end='')
        if count != 0:
            print('')
        print('};')
        print('#######################################')

    # 保存训练字符串
    def save(self):
        path = os.path.join(self.work_dir, 'train_str.txt')
        f = open(path, 'w')
        f.write(self.train_str)
        f.close()

    # 执行转换过程
    def make(self):
        self.iterate_dir()
        if len(self.train_str) > 0:
            self.output_class_table()
            self.save()
            print('train_img_cov: 字符串长度: %d' % (len(self.train_str)))
        print('train_img_cov: 转换完成!')
        print('train_img_cov: 共有 %d 种类别，共 %d 张图片' % (self.class_count, self.file_count))

# 程序入口
if __name__ == '__main__':
    # 尺寸必须是3的倍数
    imageTrainFileMake = ImageTrainFileMake(work_dir, 120, 120)
    imageTrainFileMake.make()
