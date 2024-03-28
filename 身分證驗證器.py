# 建立視窗
import tkinter as tk
root=tk.Tk()
root.geometry("300x300")
root.title("身分證字號驗證器")
# 變數
Id=tk.StringVar()
show=tk.StringVar()
# 建立標籤
label=tk.Label(root,text="請輸入身分證字號")
label.pack()
# 建立輸入藍
entry=tk.Entry(root,textvariable=Id)
entry.pack()
result=""
id=""
def clear():
    Id.set('')
    show.set("")               
    entry.delete(0,'end') 
def verify():
    global result
    global id
    id=Id.get()
    result=""
    if len(id)>1:
        a=id[0].upper()
        fn="ABCDEFGHJKLMNPQRSTUVXYWZIO".find(a)+10
    x=0
    arr=0
    y=0
    if len(id)==10 and a in "ABCDEFGHJKLMNPQRSTUVXYWZIO":
        for i in range(1,10):
            if id[i] in"1234567890":
                x=x+1
        if x==9:      
            for i in range(1,10):
                arr=arr+(int(id[i])*(8-y))
                if y<7:
                    y=y+1
            x1=fn//10
            x2=fn%10
            arr=arr+x1+x2*9
            sex=""
            if id[1]=="1":
                sex="男"
            else:
                sex="女"
            if arr%10==0:
                result=result+"此身分證字號[正確],性別為"+sex
                show.set(result)
            else:
                result=result+"此為[不正確]的身分證字號"
                show.set(result)
        else:
            result=result+"輸入格式錯誤"
            show.set(result)
    else:
        result=result+"輸入長度錯誤"
        show.set(result)
button1=tk.Button(root,text="確定",command=verify)
button1.place(x=100,y=50)
button2=tk.Button(root,text="清除",command=clear)
button2.place(x=150,y=50)

label_out=tk.Label(root,textvariable=show,font=13,fg="red")
label_out.place(x=10,y=100)
root.mainloop()