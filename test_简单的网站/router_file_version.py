from test_flask.test_简单的网站 import cmd_file
import json
from flask_cors import cross_origin
import os
from flask import Blueprint,render_template
router_file_version= Blueprint('router_file_version', __name__)

# 文件夹版本，index.html中请求文件夹版本
@router_file_version.route("/1")
def birthday10_12():
    return render_template("test2.html")


# 文件夹版本，获取文件名，日期，图片数据
@router_file_version.route("/getStaffs1")
def getStaffs1():
    os.chdir(os.path.dirname(__file__))
    print(os.getcwd(),'========================================================')
    dir_path1 = './static/img'
    # 获取path下的文件名或者文件名
    l1 = cmd_file.getImgs(dir_path1)
    obj1 = {'info': l1}
    l2 = {}
    for i in range(len(l1)):
        # print(l1[i],'----------------------------')
        dir_path2 = './static/img/'+l1[i]
        # print(dir_path2,'----------------------------------')
        # 获取path下的文件或目录的绝对路径
        l2[l1[i]] = cmd_file.getPathFile(dir_path2)
        # print(dir_path2,cmd_file.getPathFile(dir_path2),'======================')
    print(l2,'-------------------------------------------------')
    return json.dumps(l2)


# 文件夹版本，获取static目录下的文件夹名称
@router_file_version.route("/getStaffs")
def getStaffs():

    dir_path1 = os.path.dirname(__file__)+'/static/img'
    l1 = cmd_file.getImgs(dir_path1)
    obj1 = {'info': l1}
    return json.dumps(obj1)
    # return obj1


# 文件夹版本，移动数据库到指定名字文件夹，para中内容为文件名
@router_file_version.route("/mvImg/<para>")
def mvImg(para):
    print('mvImg方法访问到了，参数是',para)
    dict_para = para.split('=')
    src_file='./static/img/'+dict_para[0]+'/'+dict_para[1]

    dst_path='./static/img/'+dict_para[2]+'/'
    # if dst_path.endswith('img//'):
    #     print(dst_path,'=============================================================================')
    #     return '目标目录名不对'
    s = cmd_file.mymovefile(src_file,dst_path)
    return s

# @app.route("/getImages/<name>")
# def getImages(name):
#     dir_path = './static/img/'+name
#     l1 = cmd_file.getImgs(dir_path)
#     obj = {'info': l1}
#     return obj
# flask的5种返回值
# https://article.itxueyuan.com/56bMj9