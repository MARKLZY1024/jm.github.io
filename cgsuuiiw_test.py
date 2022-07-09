import hashlib
import random
list_1 = "qazwsxedcrfvtgbyhnujmikolp"
list_2 = "2431568790"
def md5(content=None):
    if content is None:
        return ''
    md5gen = hashlib.md5()
    md5gen.update(content.encode())
    md5code = md5gen.hexdigest()
    md5gen = None
    return md5code

def sp_98():
    oipu = ""
    superuserm = str(input("输入超级管理员密码："))
    if md5(superuserm) == "6a8d29e1a5b532b8b1bf061d7c32dcb5":
        print("登录成功！")
        for i in range(10):
            b = random.randint(1,50)
            list_928772663 = 'g28y782gfe$^%^&@&@*(ue1287828(!wbhwiuhi6963T&*HW{@>:Q<?>2guywfQ:<Q":L}O@(wbygwuyU@(*@^&R^@%^ywgyuTRDt)))'
            for i in range(b):
                a = random.randint(1,100)
                wyui = list_928772663[a]
                oipu += wyui
            sr_1 = oipu 
            die = md5(sr_1)
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



            a1 = onlyonedm_0
            with open('注册码.txt', mode='a') as f:
                f.write(a1 + "\n")
            print(onlyonedm_0)
        print("写入成功")
    else:
        print("#*#成！功？#*#")