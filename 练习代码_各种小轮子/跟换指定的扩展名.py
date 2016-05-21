#-*- coding=utf-8 -*-
import os
def change_ext(path,old_ext,new_ext):
    '''

    :param path: 路径
    :param old_ext: 替换前的扩展名
    :param new_ext: 替换后的扩展名
    :return: 重命名
    '''
    if os.path.isdir(path):
        dir=os.listdir(path)
        for i in dir:
            pathname=os.path.join(path,i)
            change_ext(pathname,old_ext,new_ext)
    elif os.path.isfile(path):
        filename=os.path.split(path)
        list_filename=(filename[1]).split('.')
        try:# 处理没有后缀名的文件
            ext=list_filename[1]
        except:
            ext=None
        if ext==old_ext:
            #更换名字，重新组装路径
			#这里注意一个坑：join的时候需要把finename[0]放在后面，因为他是一个tuple的元素，不是路径了，所以必须放在后面
            os.rename(path,os.path.join("",filename[0]+"//"+list_filename[0]+'.'+new_ext))
    else:
        print('请输入正确的路径或者文件名')
change_ext('.','test','1')