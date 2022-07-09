# -*- coding: utf8 -*-
import cryptocode
import hashlib
list_1 = "qazwsxedcrfvtgbyhnujmikolp"
list_2 = "2431568790"


def jmt_11():
    sr_1 = str(input("输入需加密文件："))
    sr_mm = str(input("输入密码："))
    
    def md5(content=None):
        if content is None:
            return ''
        md5gen = hashlib.md5()
        md5gen.update(content.encode())
        md5code = md5gen.hexdigest()
        md5gen = None
        return md5code
    die = md5(sr_1)
    print("账户：",die)
    def onlyonedm():
        die_2 = die
        onlyonedm_1 = ""
        for i in range(4):
            for n in die_2[i*3:3*(i+1)]:
                try:
                    onlyonedm_1 += list_1[int(n)]
                except:
                    onlyonedm_1 += n
            for n in die_2[i*5:5*(i+1)]:
                try:
                    onlyonedm_1 += list_2[int(n)]
                except:
                    onlyonedm_1 += str(list_1.find(n))
            if i < 3:
                onlyonedm_1 += "-"

        return onlyonedm_1
    onlyonedm_0 = onlyonedm()
    print("序列码：",onlyonedm_0)
    str_encoded = cryptocode.encrypt(sr_1,sr_mm)
    print("密码:",sr_mm)
    print("加密串:",str_encoded)
    
def jmf_22():
    sr_1 = str(input("输入加密文件："))
    sr_mm = str(input("输入密码："))
    str_decoded = cryptocode.decrypt(sr_1, sr_mm)
    print(str_decoded)
def yuncun():
    sr_1 = str(input("输入账户："))
    sr_mm = str(input("输入账户密码："))
    die_2 = sr_1
    onlyonedm_1 = ""
    for i in range(4):
        for n in die_2[i*3:3*(i+1)]:
            try:
                onlyonedm_1 += list_1[int(n)]
            except:
                onlyonedm_1 += n
        for n in die_2[i*5:5*(i+1)]:
            try:
                onlyonedm_1 += list_2[int(n)]
            except:
                onlyonedm_1 += str(list_1.find(n))
        if i < 3:
            onlyonedm_1 += "-"

    if onlyonedm_1 == sr_mm:
        f = open(str(sr_1)+".txt","r")   #设置文件对象
        str_1 = f.read()     #将txt文件的所有内容读入到字符串str中
        f.close()   #将文件关闭
        qqqq = str(input("需要密码(如果不需要密码，请输入n):"))
        if qqqq == "n":
            print(str_1)
        else:
            sr_1 = str_1
            sr_mm = qqqq
            str_decoded = cryptocode.decrypt(sr_1, sr_mm)
            print(str_decoded)
    else:
        print("错误!")
def cyun():
    sr_1 = str(input("输入需存贮文件："))
    sr_mm = str(input("输入账户："))
    with open(sr_mm+'.txt','w') as f:    #设置文件对象
        f.write(sr_1)
    
while True:
    xqiu = str(input("加密或解密(t/f),服务器读取+1(t1/f1):"))
    if xqiu == "t":
        jmt_11()
    elif xqiu == "f":
        jmf_22()
    elif xqiu == "f1":
        try:
            yuncun()
        except:
            print("none")
    elif xqiu == "t1":
        cyun()
    else:
        print("非法输入!")
        break