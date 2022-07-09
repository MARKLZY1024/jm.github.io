# -*- coding: utf8 -*-
import hashlib
def md5(content=None):
    if content is None:
        return ''
    md5gen = hashlib.md5()
    md5gen.update(content.encode())
    md5code = md5gen.hexdigest()
    md5gen = None
    return md5code
def mkdir(path):
    '''
    创建指定的文件夹
    :param path: 文件夹路径，字符串格式
    :return: True(新建成功) or False(文件夹已存在，新建失败)
    '''
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
         # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False



def cjzh_vip():
    vipz = str(input("起个名字："))
    path = "yonhumin_xwe3r4332dr3.txt"
    txt = open(path, "r", encoding="UTF-8")
    txt_list = []
    for line in txt.readlines():
        # txt.readlines()读取整个文件，返回数据中每一行有\n存在，需使用line.strip去掉
        # readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存
        line = line.strip()   # 去掉每行头尾空白
        txt_list.append(str(line))
        txt.close()
    if vipz not in txt_list:
        uytuu = vipz
        vipm = str(input("输入序列码："))
        path = "注册码.txt"
        txt = open(path, "r", encoding="UTF-8")
        xlmlist = []
        for line in txt.readlines():
            # txt.readlines()读取整个文件，返回数据中每一行有\n存在，需使用line.strip去掉
            # readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存
            line = line.strip()   # 去掉每行头尾空白
            xlmlist.append(str(line))
            txt.close()
        if vipm in xlmlist:
            gtyu = vipm
            print("序列码合法！")
            with open('yonhumin_xwe3r4332dr3.txt', 'a') as f: # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
                f.write(uytuu + "\n")
            mkdir(vipz)
            mmwj = str(input("创建一个密码:"))
            mmwj = md5(mmwj)
            with open(vipz + "/" + vipz +'_mm.txt','w') as f:    #设置文件对象
                f.write(mmwj)
            path = "注册码.txt"
            txt = open(path, "r", encoding="UTF-8")
            xlmlist_1 = []
            for line in txt.readlines():
                # txt.readlines()读取整个文件，返回数据中每一行有\n存在，需使用line.strip去掉
                # readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存
                line = line.strip()   # 去掉每行头尾空白
                xlmlist_1.append(str(line))
                txt.close()
            path = "注册码.txt"
            txt = open(path, "r", encoding="UTF-8")
            xlmlist_2 = txt.readlines()
            with open('注册码.txt','w') as f:    #设置文件对象
                f.write("")
            ee = xlmlist_1.index(gtyu)
            del xlmlist_2[ee]
            f=open("注册码.txt","w")
            f.writelines(xlmlist_2)
            f.close()            
        else:
            print("序列码错误!")
    else:
        print("账户名已存在!")

