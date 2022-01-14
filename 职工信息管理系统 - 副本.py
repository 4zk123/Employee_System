"""职工信息管理系统"""
import datetime as dt
aaa = 1000
sex=['男','女']
marrige=['已婚','未婚']
grade=['1','2','3','4','5']
tired=['在职','退休']
workage=['']
age=['']
wage=['']
name=['']
class Node:
    def __init__(self):
        self.number=1
        self.name=None
        self.sex=None
        self.age=None
        self.workage=None
        self.marrige=None
        self.grade=None
        self.wage=None
        self.tired= None
        self.next=None
class Manage_System:
    def __init__(self):
        self.head=Node()
        self.head.next=None
    def screate(self):
        x=input("请输入创建职工数目：")
        z=int(x)
        for i in range(z):
            n=self.head.next
            p=Node()
            global aaa
            aaa = aaa +1
            p.number=aaa
            p.name=input("请输入职工姓名：")
            p.age=input("请输入职工年龄：")
            p.workage=input("请输入职工工龄：")
            p.sex=input("请输入职工性别；男/女：")
            p.marrige=input("请输入职工婚姻状况：已婚/未婚：")
            p.grade=input("请输入职工等级：1-5：")
            p.wage=input("请输入职工薪资：")
            p.tired=input("请输入职工是否在职：在职/退休：")
            p.next=None
            if p.sex in sex and p.marrige in marrige and p.grade in grade and p.tired in tired and p.workage not in workage and p.name not in name and p.age not in age and p.wage not in wage:
                p.next=self.head.next
                self.head.next=p
                print("创建成功！")
            else:
                print("创建信息有误，返回开始界面。")
    def add_one(self):
        n=self.head.next
        p=Node()
        global aaa
        aaa = aaa +1
        p.number=aaa
        p.name=input("请输入职工姓名：")
        p.age=input("请输入职工年龄：")
        p.workage=input("请输入职工工龄：")
        p.sex=input("请输入职工性别；男/女：")
        p.marrige=input("请输入职工婚姻状况：已婚/未婚：")
        p.grade=input("请输入职工等级：1-5：")
        p.wage=input("请输入职工薪资：")
        p.tired=input("请输入职工是否在职：在职/退休：")
        p.next=None
        if p.sex in sex and p.marrige in marrige and p.grade in grade and p.tired in tired and p.workage not in workage and p.name not in name and p.age not in age and p.wage not in wage:
            print("如果想继续添加员工信息请选1,返回开始界面请选2.")
            p.next=self.head.next
            self.head.next=p
            a=input()
            if a=='1':
                self.add_one()
            elif a=='2':
                print("返回开始界面")
            else:
                aaa=aaa-1
                print("输入错误，返回开始界面")
        else:
            print("添加信息有误，返回开始界面。")
    def sshow(self):
        print("姓名查询请选1，工龄查询请选2，级别查询请选3")
        a=input("请输入选项：")
        if a=='1':
            b=input("请输入员工姓名：")
            d=self.head.next
            while 1:
                if d==None:
                    print("查无此人")
                    break
                elif b!=d.name:
                    d=d.next
                elif b==d.name:
                    print("\nID",d.number,end=" ")
                    print("姓名",d.name,end=" ")
                    print("年龄",d.age,end=" ")
                    print("工龄",d.workage,end=" ")
                    print("性别",d.sex,end=" ")
                    print("婚姻状况",d.marrige,end=" ")
                    print("等级",d.grade,end=" ")
                    print("薪资",d.wage,end=" ")
                    print("在职情况",d.tired,end=" ")
                    break
        elif a=='2':
            b=input("请输入员工工龄：")
            d=self.head.next
            while 1:
                if d==None:
                    print("查无此人")
                    break
                elif b!=d.workage:
                    d=d.next
                elif b==d.workage:
                    print("\nID",d.number,end=" ")
                    print("姓名",d.name,end=" ")
                    print("年龄",d.age,end=" ")
                    print("工龄",d.workage,end=" ")
                    print("性别",d.sex,end=" ")
                    print("婚姻状况",d.marrige,end=" ")
                    print("等级",d.grade,end=" ")
                    print("薪资",d.wage,end=" ")
                    print("在职情况",d.tired,end=" ")
                    break
        elif a=='3':
            b=input("请输入员工级别：")
            d=self.head.next
            while 1:
                if d==None:
                    print("查无此人")
                    break
                elif b!=d.grade:
                    d=d.next
                elif b==d.grade:
                    print("\nID",d.number,end=" ")
                    print("姓名",d.name,end=" ")
                    print("年龄",d.age,end=" ")
                    print("工龄",d.workage,end=" ")
                    print("性别",d.sex,end=" ")
                    print("婚姻状况",d.marrige,end=" ")
                    print("等级",d.grade,end=" ")
                    print("薪资",d.wage,end=" ")
                    print("在职情况",d.tired,end=" ")
                    break
        else:
            print("输入错误，返回菜单。")
    def update(self):
        a=input("\n请输入被修改职工ID：")
        b=int(a)
        d=self.head.next
        while 1:
            if d==None:
                print("查无此人信息")
                break
            elif b!=d.number:
                d=d.next
            elif b==d.number:
                print("\n修改年龄请选1")
                print("修改工龄请选2")
                print("修改性别请选3")
                print("修改婚姻状况请选4")
                print("修改等级请选5")
                print("修改薪资请选6")
                print("修改在职情况请选7")
                print("退出程序请选8")
                b=input("请输入选项：")
                if b=='1':
                    c=input("请输入修改信息：")
                    d.age=c
                    print("\nID",d.number,end=" ")
                    print("姓名",d.name,end=" ")
                    print("年龄",d.age,end=" ")
                    print("工龄",d.workage,end=" ")
                    print("性别",d.sex,end=" ")
                    print("婚姻状况",d.marrige,end=" ")
                    print("等级",d.grade,end=" ")
                    print("薪资",d.wage,end=" ")
                    print("在职情况",d.tired,end=" ")
                    break
                elif b=='2':
                    c=input("请输入修改信息：")
                    d.workage=c
                    print("\nID",d.number,end=" ")
                    print("姓名",d.name,end=" ")
                    print("年龄",d.age,end=" ")
                    print("工龄",d.workage,end=" ")
                    print("性别",d.sex,end=" ")
                    print("婚姻状况",d.marrige,end=" ")
                    print("等级",d.grade,end=" ")
                    print("薪资",d.wage,end=" ")
                    print("在职情况",d.tired,end=" ")
                    break
                elif b=='3':
                    c=input("请输入修改信息：")
                    if c in sex:
                        d.sex=c
                        print("\nID",d.number,end=" ")
                        print("姓名",d.name,end=" ")
                        print("年龄",d.age,end=" ")
                        print("工龄",d.workage,end=" ")
                        print("性别",d.sex,end=" ")
                        print("婚姻状况",d.marrige,end=" ")
                        print("等级",d.grade,end=" ")
                        print("薪资",d.wage,end=" ")
                        print("在职情况",d.tired,end=" ")
                        break
                    else:
                        print("输入错误")
                        break
                elif b=='4':
                    c=input("请输入修改信息：")
                    if c in marrige:
                        d.marrige=c
                        print("\nID",d.number,end=" ")
                        print("姓名",d.name,end=" ")
                        print("年龄",d.age,end=" ")
                        print("工龄",d.workage,end=" ")
                        print("性别",d.sex,end=" ")
                        print("婚姻状况",d.marrige,end=" ")
                        print("等级",d.grade,end=" ")
                        print("薪资",d.wage,end=" ")
                        print("在职情况",d.tired,end=" ")
                        break
                    else:
                        print("输入错误")
                        break
                elif b=='5':
                    c=input("请输入修改信息：")
                    if c in grade:
                        d.grade=c
                        print("\nID",d.number,end=" ")
                        print("姓名",d.name,end=" ")
                        print("年龄",d.age,end=" ")
                        print("工龄",d.workage,end=" ")
                        print("性别",d.sex,end=" ")
                        print("婚姻状况",d.marrige,end=" ")
                        print("等级",d.grade,end=" ")
                        print("薪资",d.wage,end=" ")
                        print("在职情况",d.tired,end=" ")
                        break
                    else:
                        print("输入错误")
                        break
                elif b=='6':
                    c=input("请输入修改信息：")
                    d.wage=c
                    print("\nID",d.number,end=" ")
                    print("姓名",d.name,end=" ")
                    print("年龄",d.age,end=" ")
                    print("工龄",d.workage,end=" ")
                    print("性别",d.sex,end=" ")
                    print("婚姻状况",d.marrige,end=" ")
                    print("等级",d.grade,end=" ")
                    print("薪资",d.wage,end=" ")
                    print("在职情况",d.tired,end=" ")
                    break
                elif b=='7':
                    c=input("请输入修改信息：")
                    if c in tired:
                        d.tired=c
                        print("\nID",d.number,end=" ")
                        print("姓名",d.name,end=" ")
                        print("年龄",d.age,end=" ")
                        print("工龄",d.workage,end=" ")
                        print("性别",d.sex,end=" ")
                        print("婚姻状况",d.marrige,end=" ")
                        print("等级",d.grade,end=" ")
                        print("薪资",d.wage,end=" ")
                        print("在职情况",d.tired,end=" ")
                        break
                    else:
                        print("输入错误")
                        break
                elif b=='8':
                    print("退出程序。")
                    break
                else:
                    print("输入错误，请重新输入")
                    ms.update()
    def sort(self):
        d=self.head.next
        print("\n输出职工信息",end=" ")
        while d!=None:
            print("\nID",d.number,end=" ")
            print("姓名",d.name,end=" ")
            print("年龄",d.age,end=" ")
            print("工龄",d.workage,end=" ")
            print("性别",d.sex,end=" ")
            print("婚姻状况",d.marrige,end=" ")
            print("等级",d.grade,end=" ")
            print("薪资",d.wage,end=" ")
            print("在职情况",d.tired,end=" ")
            d=d.next
    def dels(self):
        a=input("请输入被删除员工ID：")
        r=self.head.next
        s=self.head
        b=int(a)
        while 1:
            if r==None:
                print("查无此人信息")
                break
            elif b==r.number:
                print("\nID",r.number,end=" ")
                print("姓名",r.name,end=" ")
                print("年龄",r.age,end=" ")
                print("工龄",r.workage,end=" ")
                print("性别",r.sex,end=" ")
                print("婚姻状况",r.marrige,end=" ")
                print("等级",r.grade,end=" ")
                print("薪资",r.wage,end=" ")
                print("在职情况",r.tired,end=" ")
                s.next=r.next
                break
            elif b!=r.number:
                r=r.next
                s=s.next
    def change_wage(self):
        s=self.head.next
        sa=0
        while 1:
            if s==None:
                break
            elif s.tired=='退休' or s.tired=='在职':
                if s.tired=='退休':
                    sa=int(s.wage)
                    s.wage=sa+50
                    print("ID:",s.number)
                    print("姓名：",s.name)
                    print("薪资：",s.wage)
                    s=s.next
                elif s.tired=='在职':
                    if s.grade=='1':
                        sa=int(s.wage)
                        s.wage=sa+20
                        print("ID:",s.number)
                        print("姓名：",s.name)
                        print("薪资：",s.wage)
                        s=s.next
                    elif s.grade=='2':
                        sa=int(s.wage)
                        s.wage=sa+40
                        print("ID:",s.number)
                        print("姓名：",s.name)
                        print("薪资：",s.wage)
                        s=s.next
                    elif s.grade=='3':
                        sa=int(s.wage)
                        s.wage=sa+60
                        print("ID:",s.number)
                        print("姓名：",s.name)
                        print("薪资：",s.wage)
                        s=s.next
                    elif s.grade=='4':
                        sa=int(s.wage)
                        s.wage=sa+80
                        print("ID:",s.number)
                        print("姓名：",s.name)
                        print("薪资：",s.wage)
                        s=s.next
                    elif s.grade=='5':
                        sa=int(s.wage)
                        s.wage=sa+100
                        print("ID:",s.number)
                        print("姓名：",s.name)
                        print("薪资：",s.wage)
                        s=s.next
                    else:
                        print("信息出现错误，请检查信息。")
                        break
            else:
                print(s.wage,"信息出现错误，请检查信息。")
                break
ms=Manage_System()
"管理员账户："
manage_password="7759732"
num=100000
global k
k=1
while k:
    x=1
    z=1
    while x:
        c=input("请输入口令：")    
        if c==manage_password:
            print("你是合法用户！")
            while 1:
                q=dt.datetime.now().strftime('%F %X')
                print('\n',q)
                print("********************************************************************************")
                print("*                                *                                       ")
                print("*                            欢迎使用本职工信息管理系统                        *")
                print("*   1。创建职工信息。         2.查询职工信息。   *")
                print("*   3.修改职工信息。          4,添加职工信息。   *")
                print("*   5.删除职工信息。          6.排序至关信息。   *")
                print("*   7.修改管理员口令。        8.退出程序。       *")
                print("*                                                   *                                                                         ")
                print("*                    请输入相应编号：              *")
                print("*                                                  *")
                print("********************************************************************************")
                e=input("\n请输入选项：")
                if e=='1':
                    print("创建职工信息")
                    ms.screate()
                elif e=='2':
                    print("查询职工信息")
                    ms.sshow()
                elif e=='3':
                    print("修改职工信息")
                    ms.update()
                elif e=='4':
                    print("添加职工信息")
                    ms.add_one()
                elif e=='5':
                    print("删除职工信息")
                    ms.dels()
                elif e=='6':
                    print("排序至关信息")
                    ms.sort()
                elif e=='7':
                    print("修改管理员口令")
                    ac=input("请输入修改后密码。")
                    manage_password=ac
                    print("修改成功")
                    break
                elif e=='8':
                    print("退出程序")
                    k=0
                    x=0
                    break
                elif e=='9':
                    ms.change_wage()
                else:
                    print("输入错误，返回界面。")
        elif z>2:
            print("错误次数过多！")
            k=0
            x=0
            break
        elif c!=manage_password:
            z+=1
            print("你是非法用户！")
        else:
            print("返回登录界面")
            break
