from time import *
slep=[1,5,10,30,60,300,-1]
e_s=0

def isnum(st): #没有不老实的人就没有这段代码
    dot=0
    if st[0]=="." or st[len(st)-1]==".":
        return 0
    for i in range(len(st)):
        a = st[i]
        if a!="1" and a!="2" and a!="3" and a!="4" and a!="5" and a!="6" and a!="7" and a!="8" and a!="9" and a!="0":
            if a!=".":
                return 0
            if dot:
                return 0
            dot+=1
    return 1

def wait():
    global slep
    global e_s
    tmp=slep[e_s]
    print("你不老实")
    for i in range(tmp):
        print(f"剩余{tmp-i}秒...")
        sleep(1)
    e_s+=1
    if(slep[e_s]==-1):
        print("无休止休眠")
        while(1):
            sleep(114514)

def get(st):
    while 1:
        a = input(st)
        if isnum(a):
            return a
        else:
            wait()

class calc():
    def __init__(self,a,b):
        self.a=int(a) if int(float(a))==float(a) else float(a)
        self.b=int(b) if int(float(b))==float(b) else float(b)
    def plus(self):
        res=self.a+self.b
        return int(res) if int(res)==res else res
    def minus(self):
        res=self.a-self.b
        return int(res) if int(res)==res else res
    def mult(self):
        res=self.a*self.b
        return int(res) if int(res)==res else res
    def chu(self):
        res=self.a/self.b
        return int(res) if int(res)==res else res



num=calc(get("请输入A的大小:"),get("请输入B的大小:"))
while 1:
    ys=input("运算(+,-,*,/):")
    if ys=='+':
        print(f"{num.a}+{num.b}={num.plus()}")
        break
    elif ys=='-':
        print(f"{num.a}+{num.b}={num.minus()}")
        break
    elif ys=='*':
        print(f"{num.a}+{num.b}={num.mult()}")
        break
    elif ys=='/':
        print(f"{num.a}+{num.b}={num.chu()}")
        break
    else:
        print("?")
        wait()