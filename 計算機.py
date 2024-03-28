import tkinter as tk
import tkinter.messagebox as messagebox  #載入對話框模組
root=tk.Tk()
root.geometry("305x465")
root.title("計算機")
# 變數區
number_out=tk.IntVar()
# 顯示區
label_out=tk.Label(root,textvariable=number_out,font=22,padx=130,pady=40)
label_out.pack()
def show(): #設定一個100毫秒跑一次的變數
    if len(ar1)>=1 and len(add)>=1 and len(arr)==0:
        number_out.set(add+" "+ar2)
        root.after(100, show)
    elif len(arr)>=1:
        number_out.set(arr)
        root.after(100, show)
    else:
        number_out.set(ar1)
        root.after(100, show) 
   
# 按鈕功能區
ar1="" # 數字1
ar2="" #數字2 
add="" # 加減乘除
arr="" # 數字1+數字2=總和
def number_button_1():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        ar1=ar1+"1"
        return ar1
    elif len(arr)>=1:
        ar1="1"
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"1"
        return ar2
def number_button_2():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        ar1=ar1+"2"
        return ar1
    elif len(arr)>=1:
        ar1="2"
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"2"
        return ar2
def number_button_3():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        ar1=ar1+"3"
        return ar1
    elif len(arr)>=1:
        ar1="3"
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"3"
        return ar2
def number_button_4():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        ar1=ar1+"4"
        return ar1
    elif len(arr)>=1:
        ar1="4"
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"4"
        return ar2
def number_button_5():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        ar1=ar1+"5"
        return ar1
    elif len(arr)>=1:
        ar1="5"
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"5"
        return ar2
def number_button_6():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        ar1=ar1+"6"
        return ar1
    elif len(arr)>=1:
        ar1="6"
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"6"
        return ar2
def number_button_7():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        ar1=ar1+"7"
        return ar1
    elif len(arr)>=1:
        ar1="7"
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"7"
        return ar2
def number_button_8():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        ar1=ar1+"8"
        return ar1
    elif len(arr)>=1:
        ar1="8"
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"8"
        return ar2
def number_button_9():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        ar1=ar1+"9"
        return ar1
    elif len(arr)>=1:
        ar1="9"
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"9"
        return ar2
def number_button_0():
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        if len(ar1)==0:
            a=0    
        else:    
            ar1=ar1+"0"
            return ar1
    elif len(arr)>=1:
        ar1=""
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"0"
        return ar2
def number_button_decimal(): #小數點[.]
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        if len(ar1)==0:
            a=0    
        else:    
            ar1=ar1+"."
            return ar1
    elif len(arr)>=1:
        ar1=""
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2+"."
        return ar2
def button_add(): # 加法 [+]
    global ar1
    global ar2
    global add
    global arr
    if len(arr)==0 and len(ar2)==0:
        add="+"
    elif  len(ar1)>=1 and len(ar1)>=1 and len(arr)==0:
        if "." in ar1 or "." in ar2:
            arr=str(float(ar1)+float(ar2))
            ar1=arr
            ar2=""
            arr=""
            add="+"
            return add,ar1,ar2,arr
        else:
            arr=str(int(ar1)+int(ar2))
            ar1=arr
            ar2=""
            arr=""
            add="+"
            return add,ar1,ar2,arr
           
    else:
        ar1=arr
        ar2=""
        arr=""
        add="+"
    return add,ar1,ar2,arr
def button_Sub(): # 減法 [-]
    global ar1
    global ar2
    global add
    global arr
    if len(arr)==0 and len(ar2)==0:
        add="一"
    elif  len(ar1)>=1 and len(ar1)>=1 and len(arr)==0:
        if "." in ar1 or "." in ar2:
            arr=str(float(ar1)-float(ar2))
            ar1=arr
            ar2=""
            arr=""
            add="一"
            return add,ar1,ar2,arr
        else:
            arr=str(int(ar1)-int(ar2))
            ar1=arr
            ar2=""
            arr=""
            add="一"
            return add,ar1,ar2,arr
           
    else:
        ar1=arr
        ar2=""
        arr=""
        add="一"
    return add,ar1,ar2,arr
def button_mul(): # 乘法 [X]
    global ar1
    global ar2
    global add
    global arr
    if len(arr)==0 and len(ar2)==0:
        add="X"
    elif  len(ar1)>=1 and len(ar1)>=1 and len(arr)==0:
        if "." in ar1 or "." in ar2:
            arr=str(float(ar1)*float(ar2))
            ar1=arr
            ar2=""
            arr=""
            add="X"
            return add,ar1,ar2,arr
        else:
            arr=str(int(ar1)*int(ar2))
            ar1=arr
            ar2=""
            arr=""
            add="X"
            return add,ar1,ar2,arr
           
    else:
        ar1=arr
        ar2=""
        arr=""
        add="X"
    return add,ar1,ar2,arr
def button_div(): # 除法 [÷]
    global ar1
    global ar2
    global add
    global arr
    if len(arr)==0 and len(ar2)==0:
        add="÷"
    elif  len(ar1)>=1 and len(ar1)>=1 and len(arr)==0:
        if "." in ar1 or "." in ar2:
            arr=str(float(ar1)/float(ar2))
            ar1=arr
            ar2=""
            arr=""
            add="÷"
            return add,ar1,ar2,arr
        else:
            arr=str(int(ar1)/int(ar2))
            ar1=arr
            ar2=""
            arr=""
            add="÷"
            return add,ar1,ar2,arr
           
    else:
        ar1=arr
        ar2=""
        arr=""
        add="÷"
    return add,ar1,ar2,arr
def button_sum(): # 等於[=]
    global ar1
    global ar2
    global arr
    global add
    if len(ar1)>=1 and len(ar2)>=1:
        if "." in ar1 or "." in ar2:
            if add=="+":
                arr=str(float(ar1)+float(ar2))
                return arr 
            elif add=="X":
                arr=str(float(ar1)*float(ar2))
                return arr 
            elif add=="一":
                arr=str(float(ar1)-float(ar2))
                return arr
            elif add=="÷":
                arr=str(float(ar1)/float(ar2))
                return arr
        else:
            if add=="+":
                arr=str(int(ar1)+int(ar2))
                return arr
            elif add=="X":
                arr=str(int(ar1)*int(ar2))
                return arr
            elif add=="一":
                arr=str(int(ar1)-int(ar2))
                return arr 
            elif add=="÷":
                arr=str(int(ar1)/int(ar2))
                return arr    
def button_c(): # 刪除
    global ar1
    global ar2
    global add
    global arr
    if len(add)==0:
        if len(ar1)==0:
            a=0    
        else:    
            ar1=ar1[:-1]
            return ar1
    elif len(arr)>=1:
        ar1=""
        ar2=""
        arr=""
        add=""
        return ar1,ar2,arr,add
    else:
        ar2=ar2[:-1]
        return ar2
def button_ac(): #全部刪除
    global ar1
    global ar2
    global add
    global arr
    ar1=""
    ar2=""
    arr=""
    add=""
    return ar1,ar2,arr,add
def showcat():
    result=messagebox.askyesno("Title","            (=^･ω･^=)")
# 按鈕功能
button_1=tk.Button(root,text="←",font=13,padx=23, pady=20,command=button_c)
button_2=tk.Button(root,text="AC",font=10,padx=16, pady=20,command=button_ac)
button_3=tk.Button(root,text="   ",font=13,padx=21, pady=20)
button_4=tk.Button(root,text="÷",font=13,padx=22 ,pady=20,command=button_div)
button_5=tk.Button(root,text="7",font=13,padx=25 ,pady=20,command=number_button_7)
button_6=tk.Button(root,text="8",font=13,padx=25 ,pady=20,command=number_button_8)
button_7=tk.Button(root,text="9",font=13,padx=25 ,pady=20,command=number_button_9)
button_8=tk.Button(root,text="X",font=13,padx=21 ,pady=20,command=button_mul)
button_9=tk.Button(root,text="4",font=13,padx=25 ,pady=20,command=number_button_4)
button_10=tk.Button(root,text="5",font=13,padx=25 ,pady=20,command=number_button_5)
button_11=tk.Button(root,text="6",font=13,padx=25 ,pady=20,command=number_button_6)
button_12=tk.Button(root,text="一",font=11,padx=18 ,pady=20,command=button_Sub)
button_13=tk.Button(root,text="1",font=13,padx=25 ,pady=20,command=number_button_1)
button_14=tk.Button(root,text="2",font=13,padx=25 ,pady=20,command=number_button_2)
button_15=tk.Button(root,text="3",font=13,padx=25 ,pady=20,command=number_button_3)
button_16=tk.Button(root,text="+",font=13,padx=23 ,pady=20,command=button_add)
button_17=tk.Button(root,text="0",font=13,padx=25 ,pady=20,command=number_button_0)
button_18=tk.Button(root,text="  ",font=13,padx=24 ,pady=20,command=showcat)
button_19=tk.Button(root,text=".",font=13,padx=27 ,pady=20,command=number_button_decimal)
button_20=tk.Button(root,text="=",font=13,padx=23 ,pady=20,command=button_sum)
# 按鈕位子
button_1.place(x=5,y=110)
button_2.place(x=80,y=110)
button_3.place(x=155,y=110)
button_4.place(x=230,y=110)
button_5.place(x=5,y=180)
button_6.place(x=80,y=180)
button_7.place(x=155,y=180)
button_8.place(x=230,y=180)
button_9.place(x=5,y=250)
button_10.place(x=80,y=250)
button_11.place(x=155,y=250)
button_12.place(x=230,y=250)
button_13.place(x=5,y=320)
button_14.place(x=80,y=320)
button_15.place(x=155,y=320)
button_16.place(x=230,y=320)
button_17.place(x=5,y=390)
button_18.place(x=80,y=390)
button_19.place(x=155,y=390)
button_20.place(x=230,y=390)

show()
root.mainloop()