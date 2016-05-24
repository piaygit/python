#-*— coding=utf-8 -*-
from PIL import Image

# 灰度值 = 0.2126 * r + 0.7152 * g + 0.0722 * b
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>")
def get_char(r,b,g):
    # RGB的值转换为字符函数
    # 将256灰度映射到70个字符上
    length=len(ascii_char)
    gray=int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit=(256.0+1)/length
    return ascii_char[int(gray/unit)]
if __name__=='__main__':
    im=Image.open('./qinghimingyue6.jpg')
    w,h=im.size
    pix=im.load()
    txt=''
    for i in xrange(w):
        for j in xrange(h):
            rgb=pix[i,j] # 得到这个坐标点的rgb颜色
            txt+=get_char(rgb[0],rgb[1],rgb[2])
        txt+='\n'
    print txt
# 字符画输入到文件

with open('output.txt',"w+") as f:
    f.write(txt)




