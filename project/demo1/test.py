'''Python 代码完成生成马赛克图片的脚本。 通过本实验将学习到什么是 RGB 与 HSV 色彩空间，Python 基础，
包括 pillow 库的使用、多进程库 multiprocessing 的使用，制作马赛克图像的原理Python 代码完成生成马赛克图片的脚本。
 通过本实验将学习到什么是 RGB 与 HSV 色彩空间，Python 基础，包括 pillow 库的使用、多进程库 multiprocessing 的使用，
 制作马赛克图像的原理


 知识点：
    RGB 色彩空间与 HSV 色彩空间互相转化。
    Python 多进程的使用。
    Python 图像处理库 Pillow 的使用。
    使用 Python 制作马赛克样式的图片。

Python 3.5.2
numpy==1.18.1
Pillow==8.0.0

原理： 一张图像是通过许多的像素组成的。 为了生成马赛克图片，我们的想法是，
    将原有图像的每一个小部分，使用颜色与这一小部分相似的图像进行替换，从而生成马赛克风格的图像

'''

s1 = '''
RGB 色彩空间 （红绿蓝 三基色 --》 0 -- 255)

亮度 --》 修改三基色 （不能方便比较颜色的相似度） 255，255，255

HSV 色彩空间  分量组成： Hue 色调 ， Saturation 饱和度 颜色的深浅, value 明度

圆柱体表示 ： H 极坐标 极角 ，S 轴的长度 ，V 高度 （颜色的明暗程度）

---》 黄色 --》 H 决定 H =60,S =100%, V=100%  黄色

转换关系：
    max= max(R,G,B)
    min= min(R,G,B)
    
    V = max , S  = max -min / max ; =0
    h = 60 * (0 + G-B/max-min), if MAX=R
    h = 60 * (2 + B-R/max-min), if MAX=G
    h = 60 * (4 + R-G/max-min), if MAX=B
    
rgb --- 转换 ---》 RGB / 255 --> hsv 0--1 之间

1. 先提取 ： h =60 


实验步骤：
    1. 生成图像素材数据库
    2. 原图分块分析，与图像数据库对比--》 最近的图片替换
'''
