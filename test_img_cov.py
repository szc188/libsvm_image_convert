# coding=utf-8

import os
import shutil
from PIL import Image
import numpy as np
import sys

work_dir = "test_images"
img_width = 120
img_higth = 120

# try:
#     work_dir = sys.argv[1]
# except:
#     print('用法:\ttest_img_cov.py [路径]')
#     exit(1)

# 将图片转换为训练字符串
def img_to_str(image):
    count = 1
    img_str = ''
    for item in image.getdata():
        img_str = img_str + '%d' % count + ':' + '%d' % item + ' '
        count = count + 1
    return img_str

# 将图片快速重采样  3x3的格子 取四角和中心点的平均
def img_resample(image):
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

# 保存训练字符串
def save(str, path):
    path = os.path.join(path, '1_test_str.txt')
    f = open(path, 'w')
    f.write(str)
    f.close()

# 程序入口
if __name__ == '__main__':
    file_count = 0
    test_img_str = ''
    for parent, _, filenames in os.walk(work_dir):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            # try:
            #     file_path.index('.JPG')
            # except:
            #     continue
            try:
                image = Image.open(file_path)
                if image.width != img_width or image.height != img_higth:
                    print('test_img_cov: 图片尺寸不匹配(%d x %d)，调整大小' % (image.width, image.height))
                    image = image.resize(size=(img_width, img_higth))
                image = image.convert('L')
                image = img_resample(image)
                # image.show()
                str = '%d ' % file_count + img_to_str(image) + '\n'
                test_img_str = test_img_str + str
                file_count = file_count + 1
            except:
                pass
            
    if len(test_img_str) > 0:
        print('test_img_cov: 字符串长度: %d' % (len(test_img_str)))
        save(test_img_str, work_dir)

    print('test_img_cov: 转换完成!')
    print('test_img_cov: 共有 %d 张图片' % (file_count))
