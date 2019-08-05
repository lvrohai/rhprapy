# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ascii.py

from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument("file")
# 输出文件
parser.add_argument("-o","--output")
# 输出字符画宽
parser.add_argument("--width", type=int, default=80)
# 输出字符画高
parser.add_argument("--height", type=int, default=80)

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return " "
    length = len(ascii_char)
    # 将 RGB 值转为灰度值 gray，灰度值范围为 0-255
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    # 灰度值范围为 0-255，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    # 使用 PIL 的 Image.open 打开图片文件，获得对象 im
    im = Image.open(IMG)
    # 使用 PIL 库的 im.resize() 调整图片大小对应到输出的字符画的宽度和高度，注意这个函数第二个参数使用 Image.NEAREST，表示输出低质量的图片
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    txt = ""
    """
        遍历提取图片中每行的像素的 RGB 值，调用 getchar 转成对应的字符(左上角是(0,0)坐标，右下角是(∞,∞))
        im.getpixel((j,i)) 获取得到坐标 (j,i) 位置的 RGB 像素值（有的时候会包含 alpha 值），
        返回的结果是一个元组，例如 (1,2,3) 或者 (1,2,3,0)。
        我们使用 * 可以将元组作为参数传递给 get_char，
        同时元组中的每个元素都对应到 get_char 函数的每个参数。
    """
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)