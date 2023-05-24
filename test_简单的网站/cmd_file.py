import os
import shutil

dir_path='./static/img'


# 获取path下的目录名
def getImgs(path):
    l1 = []
    for file_name in os.listdir(path):
        print(file_name)
        # if os.path.isdir(file_name):
        #     l1.append(file_name)
        l1.append(file_name)
    return l1


# 获取path下的目录绝对路径和文件名的绝对路径
def getPathFile(path):
    l1 = []
    for file_name in os.listdir(path):
        print(file_name)

        l1.append(path+'/'+file_name)
    return l1


# 删除指定路径下的文件
def rmImg(path):
    # os.remove('./static/img/1_1.jpeg')
    os.remove(path)


def mymovefile(srcfile, dstpath):  # 移动函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
        return "源文件不存在 %s not exist!" % (srcfile)
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        # dst_path=dstpath + fname
        print(dstpath,'=============================================================================')
        if dstpath.endswith('img//'):
            print(dstpath, '=============================================================================')
            return '目标目录名不能为img//'
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'+dstpath)
            # return '目标目录不存在，创建目录%s' % (dstpath)
        shutil.move(srcfile, dstpath + fname)  # 移动文件
        print("move %s -> %s" % (srcfile, dstpath + fname))
        return "移动文件成功，move %s -> %s" % (srcfile, dstpath + fname)