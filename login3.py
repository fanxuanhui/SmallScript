#coding:utf-8

def OpenFile(InputUsername):
    with open('D:\E盘\study\python\jf_code\password.txt','r+') as fd:
        Line = fd.readlines()
        for item in Line:
            if item.strip().split(":")[0] == InputUsername:
                fd.close()
                return 1
            else:
                fd.close()
                return 0    

def Login():
    InputUsername = input("请输入用户名：")
    with open('D:\E盘\study\python\jf_code\password.txt','r+') as fd:
        Line = fd.readlines()
        for item in Line:
            #循环密码文件中的每一行。密码文件的格式：xxx：xxx
            #print("----此处有个bug，当注册完成后立即登陆时，程序到达这里突然不执行下去了？？---->>>")
            if item.strip().split(":")[0] == InputUsername:
                #判断输入的用户名在密码文件中存在
                CurrentPasswd = item.strip().split(":")[1]
                count = 0
                while (count < 3):
                    #三次输入密码的机会
                    InputPasswd = input("请输入密码：")
                    if CurrentPasswd == InputPasswd:
                        print("welcome to system!!")
                        break
                    else:
                        print("密码错误！！还有%s次机会输入" %(3-count-1))
                        count +=1
def register():
    #注册用户
    RUserName = input("请输入你要注册的用户名：")
    if OpenFile(RUserName) == 0:
        print("")
    else:
        print("-------用户已存在，请重新输入用户名-------")
        weclome()

    RUserPasswd = input("请输入你要注册的用户密码：")
    with open('D:\E盘\study\python\jf_code\password.txt','a+') as fd:
        fd.write(RUserName +":"+ RUserPasswd)
        fd.write("\n")
        print("你注册的用户是:%s,密码是：%s" % (RUserName,RUserPasswd))
        weclome()
        

def weclome():    
    print("""
    1、注册
    2、登陆
    """)
    action = input("请输入你的选项：")
    if action == "1":
        register()
    elif action == "2":
        Login()
    else:
        print("----输入的选项不对-----")
        weclome()

if __name__ == '__main__':   
    weclome()



