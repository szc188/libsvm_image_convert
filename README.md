# libsvm_image_convert
测试libsvm用于图片分类的python图片转换脚本

+ 测试环境: macOS Catalina

## 食用方法
**train_img_cov.py** 用于将 train_images 文件夹下的多个文件夹里的图片转换为libsvm训练的格式
最后会将txt文件保存为 train_images/train_str.txt
├── train_images
│   ├── 1
│   │   ├── IMG_9900.JPG
│   │   ├── IMG_9901.JPG
│   │   └── IMG_9905.JPG
│   ├── 2
│   │   ├── IMG_9894.JPG
│   │   ├── IMG_9895.JPG
│   │   └── IMG_9899.JPG
│   ├── 3
│   │   ├── IMG_9888.JPG
│   │   ├── IMG_9889.JPG
│   │   └── IMG_9893.JPG
│   ├── 4
│   │   ├── IMG_9881.JPG
│   │   └── IMG_9887.JPG
│   ├── 5
│   │   ├── IMG_9910.JPG
│   │   └── IMG_9911.JPG

**test_img_cov.py** 用于将 test_images 文件夹下的多个图片转换为svm-predict所需要的格式
最后会将txt文件保存为 test_images/1_test_str.txt
├── test_images
│   ├── 1_test_str.txt
│   ├── IMG_9898.JPG
│   ├── IMG_9900.JPG
│   ├── IMG_9907.JPG
│   ├── IMG_9908.JPG
│   └── IMG_9909.JPG
