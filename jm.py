import cryptocode
import hashlib
list_1 = "qazwsxedcrfvtgbyhnujmikolp"
list_2 = "2431568790"
#---------------0---------------
def md5(content=None):
        if content is None:
            return ''
        md5gen = hashlib.md5()
        md5gen.update(content.encode())
        md5code = md5gen.hexdigest()
        md5gen = None
        return md5code
#---------------1---------------
def jmt_11():
    sr_1 = str(input("输入需加密文件："))
    sr_mm = str(input("输入密码："))
    str_encoded = cryptocode.encrypt(sr_1,sr_mm)
    print("密码:",sr_mm)
    print("加密串:",str_encoded)
#---------------2---------------
def jmf_22():
    sr_1 = str(input("输入加密串："))
    sr_mm = str(input("输入密码："))
    str_decoded = cryptocode.decrypt(sr_1, sr_mm)
    print(str_decoded)
#---------------3---------------
def yuncun():
    sr = str(input("输入账户："))
    path = "yonhumin_xwe3r4332dr3.txt"
    txt = open(path, "r", encoding="UTF-8")
    txt_list = []
    for line in txt.readlines():
        # txt.readlines()读取整个文件，返回数据中每一行有\n存在，需使用line.strip去掉
        # readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存
        line = line.strip()   # 去掉每行头尾空白
        txt_list.append(str(line))
        txt.close()
    if sr in txt_list:
        file_handle=open(sr+'/'+sr+'_mm.txt',mode='r')
        content=file_handle.readline()
        sr_mm = str(input("输入账户密码："))
        sr_1 = str(input("输入文件名："))
        if md5(sr_mm) == content:
            f = open(sr+'/'+sr_1+'.txt',"r")   #设置文件对象
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
            print("密码错误")
    else:
        print("还没有这个账号")
#---------------4---------------
def cyun():
    sr_mm = str(input("输入账户："))
    sr_mm_1 = str(input("输入密码："))
    path = "yonhumin_xwe3r4332dr3.txt"
    txt = open(path, "r", encoding="UTF-8")
    txt_list = []
    for line in txt.readlines():
        # txt.readlines()读取整个文件，返回数据中每一行有\n存在，需使用line.strip去掉
        # readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存
        line = line.strip()   # 去掉每行头尾空白
        txt_list.append(str(line))
        txt.close()
    if sr_mm in txt_list:
        file_handle=open(sr_mm+'/'+sr_mm+'_mm.txt',mode='r')
        content=file_handle.readline()
        if md5(sr_mm_1) == content:
            sr_3 = str(input("输入存贮文件名："))
            sr_1 = str(input("文件内容是否加密？(y/n)："))
            if sr_1 == "y":
                sr_1 = str(input("输入需加密文件："))
                sr_mmy = str(input("输入密码："))
                str_encoded = cryptocode.encrypt(sr_1,sr_mmy)
                print("密码:",sr_mmy)
                with open(sr_mm + "/" + sr_3 +'.txt','w') as f:    #设置文件对象
                    f.write(str_encoded)
            elif sr_1 == "n":
                sr_1 = str(input("输入文件内容："))
                with open(sr_mm + "/" + sr_3 +'.txt','w') as f:    #设置文件对象
                    f.write(sr_1)
        else:
            print("密码错误！")
    else:
        print("你还没有账户！")