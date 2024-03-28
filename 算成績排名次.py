# 讀取 data1.txt 中的資料,並儲存在lines  這個list 中
lines=[i for i in open("data1.txt","r",encoding=("utf-8"))]
# 建立一個空的list d
d=[]
# 逐行讀取data1.txt 中的資料,並將資料分割成座號、姓名、國文、英文、數學、總分、平均分數、名次
# 放進一個 list t 中，最後再把 t 放到 d 這個 list 中 
for line in lines:
    no,name,ch,en,ma=line.split("  ")
    no,ch,en,ma=int(no),int(ch),int(en),int(ma)
    total =ch+en+ma
    avg=int(total/3*100+0.5)/100
    t=[no,name,ch,en,ma,total,avg,1] #最初名次設定 1
    d.append(t)
# 排列 list d 並計算每個學生的名次
for i in range(len(d)):
    for j in range(len(d)): 
        if d[i][5]<d[j][5]: 
            d[i][7]=d[i][7]+1
# 建立一個list head,用來顯示每個欄位的標題
head=["座號","  姓名","國文","英文","數學","總分","平均","名次"]
# 把list head 轉換成字串,並用tab(\t) 間隔開每個欄位
head ="\t\t".join(head)
# 顯示表格的標題
print(head)
#逐一顯示每個學生的座號、姓名、國文、英文、數學、總分、平均分數、名次
for i in d:
    t=[str(j)for j in i ]# 把每個欄位轉換成字串
    t="\t\t".join(t) # 用tab (\t)隔開每個欄位
    print(t)

"""
data1.txt
1   王小美  60  70  80
2   王二美  61  72  83
3   王大大  65  72  85
4   王詩美  61  71  82
5   王超美  65  60  80
"""