from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
import tkinter.messagebox as messagebox  #載入對話框模組
root=tk.Tk()
root.geometry("810x600")
root.title("樸克牌比大小遊戲")
# 變數區
monry_out=tk.IntVar()
monry=1000 #起始金額
rd1=[] # 1-52
gd=[] #顯示文字
j=1 # 回合數 最多25
re=0 #讀取數字
w=0 #顯示過離開訊息
# 顯示區
def show(): #設定一個100毫秒跑一次的變數
    global monry
    global j
    global w
    monry_out.set(monry)
    # 結果表格區
    hname=["回合","玩家","莊家","結果"]
    tree=ttk.Treeview(root,column=hname,show="headings")
    for i in hname:
        tree.column(i,anchor=CENTER)
        tree.heading(i,text=i)
    a=int(len(gd))//10 # 10 
    if a==0:
        b=a
    if a==1:
        b=9
    if a==2:
        b=19
    for i in range(b,len(gd)):
        tree.insert("","end",text="1",values=gd[i])
    tree.place(x=5,y=190)
    if j>=25:
        end_1()
        monry=1000
    if monry<=50 :
        end_2()
        monry=1000
    if len(rd1)==0:
        open()
    root.after(100, show)
# 開始區
def open():
    global rd1
    global gd
    global j
    a=random.randint(1,52)
    rd1.append(a)
    p=rd1[0]   #p:玩家 
    pn=p%13+1  #pn:玩家牌數字 
    pf=p//13  #pf:玩家牌花色
    rn=["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    rf=["\u2660","\u2665","\u2666","\u2663"] # 牌花色utf-8碼
    t=[j,rf[pf]+rn[pn]]
    gd.append(t)
    return gd,rd1
open()
def go():
    global rd1
    global gd
    global j
    global monry
    global re
    if j<2:
        n=0
        while True:
            a=random.randint(1,51)
            if a not in rd1:
                rd1.append(a)
                n=n+1
                if n==2:
                    break
        p=rd1[re]   #p:玩家 
        pn=p%13+1  #pn:玩家牌數字 
        pf=p//13  #pf:玩家牌花色
        re=re+1
        b=rd1[re] #b:莊家 
        bn=b%13+1  #bn:莊家牌數字 
        bf=b//13   #bf:莊家牌花色
        re=re+1
        msg=""
        if pn>bn:
            msg="玩家贏"
            monry=monry+200
        if pn==bn:
            msg="平手"
        if pn<bn:
            msg="莊家贏"
            monry=monry-200
        rn=["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        rf=["\u2660","\u2665","\u2666","\u2663"] # 牌花色utf-8碼
        t=[j,rf[pf]+rn[pn],rf[bf]+rn[bn],msg]
        del gd[-1]
        gd.append(t)
        p=rd1[re]   #p:玩家 取下一回合 
        pn=p%13+1  #pn:玩家牌數字 
        pf=p//13  #pf:玩家牌花色
        j=j+1
        t=[j,rf[pf]+rn[pn]]
        gd.append(t)
        return gd,rd1,j,monry,re
    else:
        n=0
        while True: 
            a=random.randint(1,51)
            if a not in rd1:
                rd1.append(a)
                n=n+1
                if n==2:
                    break
        p=rd1[re]   #p:玩家 
        pn=p%13+1  #pn:玩家牌數字 
        pf=p//13  #pf:玩家牌花色
        re=re+1
        b=rd1[re] #b:莊家 
        bn=b%13+1  #bn:莊家牌數字 
        bf=b//13   #bf:莊家牌花色
        re=re+1
        msg=""
        if pn>bn:
            msg="玩家贏"
            monry=monry+200
        if pn==bn:
            msg="平手"
        if pn<bn:
            msg="莊家贏"
            monry=monry-200
        rn=["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        rf=["\u2660","\u2665","\u2666","\u2663"] # 牌花色utf-8碼
        t=[j,rf[pf]+rn[pn],rf[bf]+rn[bn],msg]
        del gd[-1]
        gd.append(t)
        j=j+1
        p=rd1[re]   #p:玩家 取下一回合 
        pn=p%13+1  #pn:玩家牌數字 
        pf=p//13  #pf:玩家牌花色
        t=[j,rf[pf]+rn[pn]]
        gd.append(t)
        return gd,rd1,j,monry,re
        
def stop():
    global rd1
    global gd
    global j
    global monry
    global re
    if j<2:
        n=0
        while True:
            a=random.randint(1,51)
            if a not in rd1:
                rd1.append(a)
                n=n+1
                if n==2:
                    break
        p=rd1[re]   #p:玩家 
        pn=p%13+1  #pn:玩家牌數字 
        pf=p//13  #pf:玩家牌花色
        re=re+1
        b=rd1[re] #b:莊家 
        bn=b%13+1  #bn:莊家牌數字 
        bf=b//13   #bf:莊家牌花色
        re=re+1
        msg="棄牌"
        monry=monry-50
        rn=["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        rf=["\u2660","\u2665","\u2666","\u2663"] # 牌花色utf-8碼
        t=[j,rf[pf]+rn[pn],rf[bf]+rn[bn],msg]
        del gd[-1]
        gd.append(t)
        p=rd1[re]   #p:玩家 取下一回合 
        pn=p%13+1  #pn:玩家牌數字 
        pf=p//13  #pf:玩家牌花色
        j=j+1
        t=[j,rf[pf]+rn[pn]]
        gd.append(t)
        return gd,rd1,j,monry,re
    else:
        n=0
        while True: 
            a=random.randint(1,51)
            if a not in rd1:
                rd1.append(a)
                n=n+1
                if n==2:
                    break
        p=rd1[re]   #p:玩家 
        pn=p%13+1  #pn:玩家牌數字 
        pf=p//13  #pf:玩家牌花色
        re=re+1
        b=rd1[re] #b:莊家 
        bn=b%13+1  #bn:莊家牌數字 
        bf=b//13   #bf:莊家牌花色
        re=re+1
        msg="棄牌"
        monry=monry-50
        rn=["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        rf=["\u2660","\u2665","\u2666","\u2663"] # 牌花色utf-8碼
        t=[j,rf[pf]+rn[pn],rf[bf]+rn[bn],msg]
        del gd[-1]
        gd.append(t)
        j=j+1
        p=rd1[re]   #p:玩家 取下一回合 
        pn=p%13+1  #pn:玩家牌數字 
        pf=p//13  #pf:玩家牌花色
        t=[j,rf[pf]+rn[pn]]
        gd.append(t)
        return gd,rd1,j,monry,re

def end_1():
    global monry
    global j
    global gd
    global re
    global rd1
    global w
    msg="遊戲結束,恭喜你! 剩下金額為:"+str(monry)
    messagebox.showinfo("Title",msg)
    money=1000
    j=1
    gd=[]
    re=0
    rd1=[]
    w=0
    return j,gd,re,rd1,w,money
    
def end_2():
    global monry
    global j
    global gd
    global re
    global rd1
    global w
    msg="遊戲失敗!! !!!破產笑你小笨蛋!!!"
    messagebox.showerror("Title",msg)
    money=1000
    j=1
    gd=[]
    re=0
    rd1=[]
    w=0
    return j,gd,re,rd1,w,money
    
# 顯示區
label_1=tk.Label(root,text="(=^･ω･^=)",font=2)
label_1.place(x=360,y=30)
rule="規則:比樸克牌大小,K最大、A最小,選擇跟牌後勝出獲得200,失敗扣除200,選擇不跟牌扣除參加費50"
label_2=tk.Label(root,text=rule)
label_2.place(x=150,y=60)
label_3=tk.Label(root,text="現有金錢:",font=2)
label_3.place(x=20,y=100)
label_4=tk.Label(root,textvariable=monry_out,font=2)
label_4.place(x=115,y=100)

# 按鈕區
button_1=tk.Button(root,text="跟牌",font=2,padx=23,pady=20,command=go)
button_2=tk.Button(root,text="棄牌",font=2,padx=23,pady=20,command=stop)
button_1.place(x=300,y=90)
button_2.place(x=420,y=90)

# 最後觸發結束欄位


show()
root.mainloop()