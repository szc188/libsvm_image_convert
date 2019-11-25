# libsvm_image_convert
测试libsvm用于图片分类的python图片转换脚本

+ 测试环境: macOS Catalina

## 食用方法
**train_img_cov.py** 用于将 train_images 文件夹下的多个文件夹里的图片转换为libsvm训练的格式
最后会将txt文件保存为 train_images/train_str.txt
存放格式像下面这样
train_images/fish/1.jpg
train_images/fish/2.jpg
train_images/fish/3.jpg
train_images/fish/4.jpg
train_images/cup/1.jpg
train_images/cup/2.jpg
train_images/cup/3.jpg
train_images/cup/4.jpg
train_images/none/1.jpg
train_images/none/2.jpg
train_images/none/3.jpg
train_images/none/4.jpg


**test_img_cov.py** 用于将 test_images 文件夹下的多个图片转换为svm-predict所需要的格式
最后会将txt文件保存为 test_images/1_test_str.txt
存放格式像下面这样
test_images/1.jpg
test_images/2.jpg
test_images/3.jpg
test_images/4.jpg
